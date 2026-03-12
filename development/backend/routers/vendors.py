from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import models, schemas, database

router = APIRouter(
    prefix="/vendors",
    tags=["vendors"]
)

@router.get("/", response_model=List[schemas.VendorSchema])
def list_vendors(db: Session = Depends(database.get_db)):
    return db.query(models.Vendor).all()

@router.get("/{vendor_id}", response_model=schemas.VendorSchema)
def get_vendor(vendor_id: int, db: Session = Depends(database.get_db)):
    db_vendor = db.query(models.Vendor).filter(models.Vendor.id == vendor_id).first()
    if db_vendor is None:
        raise HTTPException(status_code=404, detail="Fornecedor não encontrado")
    return db_vendor

@router.post("/", response_model=schemas.VendorSchema)
def create_vendor(vendor: schemas.VendorCreate, db: Session = Depends(database.get_db)):
    db_vendor = models.Vendor(**vendor.dict())
    db.add(db_vendor)
    db.commit()
    db.refresh(db_vendor)
    return db_vendor

@router.put("/{vendor_id}", response_model=schemas.VendorSchema)
def update_vendor(vendor_id: int, vendor: schemas.VendorCreate, db: Session = Depends(database.get_db)):
    db_vendor = db.query(models.Vendor).filter(models.Vendor.id == vendor_id).first()
    if db_vendor is None:
        raise HTTPException(status_code=404, detail="Fornecedor não encontrado")
    
    for key, value in vendor.dict().items():
        setattr(db_vendor, key, value)
    
    db.commit()
    db.refresh(db_vendor)
    return db_vendor

@router.delete("/{vendor_id}")
def delete_vendor(vendor_id: int, db: Session = Depends(database.get_db)):
    db_vendor = db.query(models.Vendor).filter(models.Vendor.id == vendor_id).first()
    if db_vendor is None:
        raise HTTPException(status_code=404, detail="Fornecedor não encontrado")
    
    db.delete(db_vendor)
    db.commit()
    return {"message": "Fornecedor excluído com sucesso"}
