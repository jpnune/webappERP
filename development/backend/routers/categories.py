from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
import models, schemas, database

router = APIRouter(
    prefix="/categories",
    tags=["categories"]
)

@router.post("/", response_model=schemas.CategorySchema)
def create_category(category: schemas.CategoryCreate, db: Session = Depends(database.get_db)):
    db_category = db.query(models.Category).filter(models.Category.name == category.name).first()
    if db_category:
        return db_category
    
    db_category = models.Category(name=category.name)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

@router.get("/", response_model=List[schemas.CategorySchema])
def read_categories(db: Session = Depends(database.get_db)):
    return db.query(models.Category).all()

@router.delete("/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_category(category_id: int, db: Session = Depends(database.get_db)):
    db_category = db.query(models.Category).filter(models.Category.id == category_id).first()
    if not db_category:
        raise HTTPException(status_code=404, detail="Categoria não encontrada")
    db.delete(db_category)
    db.commit()
    return None
