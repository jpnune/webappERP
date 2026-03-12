import json
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import database, models, schemas

router = APIRouter(prefix="/purchases", tags=["purchases"])

@router.get("/", response_model=List[schemas.PurchaseInvoiceSchema])
def list_purchases(db: Session = Depends(database.get_db)):
    return db.query(models.PurchaseInvoice).order_by(models.PurchaseInvoice.created_at.desc()).all()

@router.post("/", response_model=schemas.PurchaseInvoiceSchema)
def create_purchase(purchase: schemas.PurchaseInvoiceCreate, db: Session = Depends(database.get_db)):
    # 1. Criar a Nota Fiscal
    db_invoice = models.PurchaseInvoice(
        invoice_number=purchase.invoice_number,
        vendor_id=purchase.vendor_id,
        purchase_date=purchase.purchase_date,
        total_amount=purchase.total_amount,
        shipping_cost=purchase.shipping_cost,
        notes=purchase.notes,
        status="completed"
    )
    db.add(db_invoice)
    db.flush() # Para pegar o ID
    
    # 2. Processar Itens e Atualizar Estoque
    for item in purchase.items:
        db_item = models.PurchaseItem(
            invoice_id=db_invoice.id,
            product_id=item.product_id,
            quantity=item.quantity,
            cost_price=item.cost_price,
            color=item.color,
            size=item.size
        )
        db.add(db_item)
        
        # Atualizar o produto real
        product = db.query(models.Product).filter(models.Product.id == item.product_id).first()
        if product:
            # Atualiza preço de custo global (opcional, pode ser média ponderada futuramente)
            product.cost_price = item.cost_price
            
            # Atualiza as variações (estoque)
            try:
                variants = json.loads(product.variants_json) if product.variants_json else []
                updated = False
                for v in variants:
                    if v.get("color") == item.color and v.get("size") == item.size:
                        current_stock = int(v.get("stock", 0))
                        v["stock"] = current_stock + item.quantity
                        updated = True
                        break
                
                if not updated:
                    # Se não existir a variação, cria uma nova
                    variants.append({
                        "color": item.color,
                        "size": item.size,
                        "stock": item.quantity,
                        "price": product.selling_price # Assume o preço de venda atual
                    })
                
                product.variants_json = json.dumps(variants)
            except Exception as e:
                print(f"Erro ao atualizar variantes: {e}")
                
    db.commit()
    db.refresh(db_invoice)
    return db_invoice

@router.get("/{id}", response_model=schemas.PurchaseInvoiceSchema)
def get_purchase(id: int, db: Session = Depends(database.get_db)):
    db_invoice = db.query(models.PurchaseInvoice).filter(models.PurchaseInvoice.id == id).first()
    if not db_invoice:
        raise HTTPException(status_code=404, detail="Nota fiscal não encontrada")
    return db_invoice
