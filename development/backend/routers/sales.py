from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
import json
import models, schemas, database

router = APIRouter(
    prefix="/sales",
    tags=["sales"]
)

@router.post("/", response_model=schemas.Sale)
def create_sale(sale: schemas.SaleCreate, db: Session = Depends(database.get_db)):
    # 0. Verificar se o cliente existe (se houver um customer_id)
    if sale.customer_id:
        db_customer = db.query(models.Customer).filter(models.Customer.id == sale.customer_id).first()
        if not db_customer:
            raise HTTPException(status_code=404, detail="Cliente não encontrado")

    # 1. Criar a Venda
    db_sale = models.Sale(
        customer_id=sale.customer_id,
        total=sale.total,
        discount=sale.discount,
        payment_method=sale.payment_method
    )
    
    # 1. Validar Limite de Crédito se for "fiado"
    if sale.payment_method == "fiado":
        if not sale.customer_id:
            raise HTTPException(status_code=400, detail="Cliente deve ser selecionado para pagamento Fiado")
        
        db_customer = db.query(models.Customer).filter(models.Customer.id == sale.customer_id).first()
        if not db_customer.status == "Ativo":
            raise HTTPException(status_code=400, detail="Cliente inativo não pode usar Fiado")
        if not db_customer.credit_enabled:
            raise HTTPException(status_code=400, detail="Crédito não habilitado para este cliente")
            
        # Calcular total gasto para limite dinâmico
        total_spent = db.query(func.coalesce(func.sum(models.Sale.total), 0))\
            .filter(models.Sale.customer_id == sale.customer_id).scalar()
            
        # Calcular crédito já utilizado
        credit_used = db.query(func.coalesce(func.sum(models.Sale.total), 0))\
            .filter(models.Sale.customer_id == sale.customer_id)\
            .filter(models.Sale.payment_method == "fiado").scalar()
            
        suggested_limit = total_spent * (db_customer.credit_limit_rate / 100.0)
        # O limite efetivo é o manual se definido (>0), senão o sugerido
        total_limit = db_customer.manual_credit_limit if db_customer.manual_credit_limit > 0 else suggested_limit
        
        available_credit = total_limit - credit_used
        
        if sale.total > available_credit:
            from decimal import Decimal
            raise HTTPException(
                status_code=400, 
                detail=f"Limite de crédito insuficiente. Disponível: R$ {available_credit:.2f}"
            )

    db.add(db_sale)
    db.commit()
    db.refresh(db_sale)
    
    # 2. Criar os Itens e dar baixa no estoque
    for item in sale.items:
        db_item = models.SaleItem(
            sale_id=db_sale.id,
            product_id=item.product_id,
            quantity=item.quantity,
            price_at_sale=item.price_at_sale,
            color=item.color,
            size=item.size
        )
        db.add(db_item)
        
        # Baixa no estoque
        db_product = db.query(models.Product).filter(models.Product.id == item.product_id).first()
        if db_product:
            try:
                v_data = json.loads(db_product.variants_json)
                
                # 1. Baixa no estoque Geral
                current_stock = v_data.get("stock", 0)
                v_data["stock"] = max(0, current_stock - item.quantity)
                
                # 2. Baixa na grade (gradeData) se tiver cor e tamanho
                if item.color and item.size:
                    grade = v_data.get("gradeData", {})
                    if item.color in grade:
                        if item.size in grade[item.color]:
                            current_v_stock = grade[item.color][item.size]
                            grade[item.color][item.size] = max(0, current_v_stock - item.quantity)
                
                db_product.variants_json = json.dumps(v_data)
            except Exception as e:
                print(f"Erro ao atualizar estoque: {e}")
                
    db.commit()
    db.refresh(db_sale)
    return db_sale

@router.get("/", response_model=List[schemas.Sale])
def read_sales(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    return db.query(models.Sale).offset(skip).limit(limit).all()
