from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import models, schemas, database

router = APIRouter(
    prefix="/staff",
    tags=["staff"]
)

@router.get("/", response_model=List[schemas.EmployeeSchema])
def list_employees(db: Session = Depends(database.get_db)):
    return db.query(models.Employee).all()

@router.post("/", response_model=schemas.EmployeeSchema)
def create_employee(employee: schemas.EmployeeCreate, db: Session = Depends(database.get_db)):
    db_employee = models.Employee(**employee.dict())
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee

@router.get("/{employee_id}", response_model=schemas.EmployeeSchema)
def get_employee(employee_id: int, db: Session = Depends(database.get_db)):
    db_employee = db.query(models.Employee).filter(models.Employee.id == employee_id).first()
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Funcionário não encontrado")
    return db_employee

@router.put("/{employee_id}", response_model=schemas.EmployeeSchema)
def update_employee(employee_id: int, employee: schemas.EmployeeUpdate, db: Session = Depends(database.get_db)):
    db_employee = db.query(models.Employee).filter(models.Employee.id == employee_id).first()
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Funcionário não encontrado")
    
    update_data = employee.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_employee, key, value)
    
    db.commit()
    db.refresh(db_employee)
    return db_employee

@router.delete("/{employee_id}")
def delete_employee(employee_id: int, db: Session = Depends(database.get_db)):
    db_employee = db.query(models.Employee).filter(models.Employee.id == employee_id).first()
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Funcionário não encontrado")
    
    db.delete(db_employee)
    db.commit()
    return {"message": "Funcionário excluído com sucesso"}
