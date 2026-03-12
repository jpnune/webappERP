from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import List

import models, schemas
from database import get_db

router = APIRouter(
    prefix="/customers",
    tags=["customers"],
)

@router.post("/", response_model=schemas.CustomerSchema)
def create_customer(customer: schemas.CustomerCreate, db: Session = Depends(get_db)):
    db_customer = models.Customer(**customer.model_dump())
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer

@router.get("/", response_model=List[schemas.CustomerSchema])
def read_customers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    # Criamos a query base
    customers_query = db.query(
        models.Customer,
        func.coalesce(func.sum(models.Sale.total), 0).label("total_spent")
    ).outerjoin(models.Sale, models.Sale.customer_id == models.Customer.id)\
     .group_by(models.Customer.id)\
     .offset(skip).limit(limit)
    
    results = []
    for customer, total_spent in customers_query.all():
        # Converte para dict usando a estrutura do modelo
        customer_dict = {c.name: getattr(customer, c.name) for c in customer.__table__.columns}
        customer_dict["total_spent"] = total_spent
        
        # Calcula Crédito Utilizado (Soma de vendas onde payment_method é crédito)
        # Assumindo que o método de pagamento para uso de limite é "credit_limit" ou similar
        credit_sales = db.query(func.coalesce(func.sum(models.Sale.total), 0))\
            .filter(models.Sale.customer_id == customer.id)\
            .filter(models.Sale.payment_method == "fiado")\
            .scalar()
        customer_dict["credit_used"] = credit_sales
        
        # Calcula crédito dinâmico
        rate = getattr(customer, "credit_limit_rate", 0.0)
        manual = getattr(customer, "manual_credit_limit", 0.0)
        enabled = getattr(customer, "credit_enabled", False)
        status = getattr(customer, "status", "Ativo")
        
        # Bloqueio de crédito para inativos
        if status != "Ativo":
            customer_dict["calculated_credit_limit"] = 0.0
        else:
            suggested = total_spent * (rate / 100.0) if enabled else 0.0
            # Prioridade: Manual (>0) -> Sugerido
            customer_dict["calculated_credit_limit"] = manual if manual > 0 else suggested
        
        results.append(customer_dict)
    return results

@router.get("/{customer_id}", response_model=schemas.CustomerSchema)
def read_customer(customer_id: int, db: Session = Depends(get_db)):
    result = db.query(
        models.Customer,
        func.coalesce(func.sum(models.Sale.total), 0).label("total_spent")
    ).outerjoin(models.Sale, models.Sale.customer_id == models.Customer.id)\
     .filter(models.Customer.id == customer_id)\
     .group_by(models.Customer.id).first()
     
    if not result:
        raise HTTPException(status_code=404, detail="Customer not found")
        
    customer, total_spent = result
    customer_dict = {c.name: getattr(customer, c.name) for c in customer.__table__.columns}
    customer_dict["total_spent"] = total_spent
    
    # Calcula Crédito Utilizado
    credit_sales = db.query(func.coalesce(func.sum(models.Sale.total), 0))\
        .filter(models.Sale.customer_id == customer_id)\
        .filter(models.Sale.payment_method == "fiado")\
        .scalar()
    customer_dict["credit_used"] = credit_sales

    # Calcula crédito dinâmico
    rate = getattr(customer, "credit_limit_rate", 0.0)
    enabled = getattr(customer, "credit_enabled", False)
    status = getattr(customer, "status", "Ativo")
    
    if status != "Ativo":
        customer_dict["calculated_credit_limit"] = 0.0
    else:
        manual = getattr(customer, "manual_credit_limit", 0.0)
        suggested = total_spent * (rate / 100.0) if enabled else 0.0
        customer_dict["calculated_credit_limit"] = manual if manual > 0 else suggested
    
    return customer_dict

@router.put("/{customer_id}", response_model=schemas.CustomerSchema)
def update_customer(customer_id: int, customer: schemas.CustomerUpdate, db: Session = Depends(get_db)):
    db_customer = db.query(models.Customer).filter(models.Customer.id == customer_id).first()
    if db_customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
        
    for key, value in customer.model_dump().items():
        setattr(db_customer, key, value)
        
    db.commit()
    db.refresh(db_customer)
    return db_customer

@router.delete("/{customer_id}")
def delete_customer(customer_id: int, db: Session = Depends(get_db)):
    db_customer = db.query(models.Customer).filter(models.Customer.id == customer_id).first()
    if db_customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
        
    db.delete(db_customer)
    db.commit()
    return {"message": "Customer deleted successfully"}
