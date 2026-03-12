from fastapi import APIRouter, Depends, Response
from sqlalchemy.orm import Session
import csv
import io
import models, database

router = APIRouter(
    prefix="/reports",
    tags=["reports"]
)

@router.get("/sales/csv")
def export_sales_csv(db: Session = Depends(database.get_db)):
    sales = db.query(models.Sale).all()
    
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["ID", "Cliente ID", "Total", "Metodo Pagamento", "Status", "Data"])
    
    for sale in sales:
        writer.writerow([sale.id, sale.customer_id, sale.total, sale.payment_method, sale.status, sale.created_at])
    
    content = output.getvalue()
    return Response(
        content=content,
        media_type="text/csv",
        headers={"Content-Disposition": "attachment; filename=relatorio_vendas.csv"}
    )

@router.get("/stock/alerts")
def get_stock_alerts(db: Session = Depends(database.get_db)):
    import json
    products = db.query(models.Product).all()
    alerts = []
    
    for p in products:
        try:
            # Se tiver grade, analisa cada variação
            if p.variants_json:
                variants = json.loads(p.variants_json)
                for color, sizes in variants.items():
                    for size, qty in sizes.items():
                        if qty < p.min_stock:
                            alerts.append({
                                "product_id": p.id,
                                "name": p.name,
                                "variant": f"{color} - {size}",
                                "stock": qty,
                                "min_stock": p.min_stock,
                                "sku": p.sku
                            })
            else:
                # Placeholder para produto simples (se houver coluna stock no futuro)
                pass
        except:
            continue
            
    return alerts
