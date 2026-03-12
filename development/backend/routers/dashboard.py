from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import datetime, timedelta
import models, database

router = APIRouter(
    prefix="/dashboard",
    tags=["dashboard"]
)

@router.get("/stats")
def get_dashboard_stats(db: Session = Depends(database.get_db)):
    today = datetime.utcnow().date()
    start_of_day = datetime.combine(today, datetime.min.time())
    
    # 1. Básicos
    total_customers = db.query(models.Customer).count()
    new_customers_today = db.query(models.Customer).filter(models.Customer.created_at >= start_of_day).count()
    
    # 2. Vendas e Ticket Médio
    sales_today_query = db.query(func.sum(models.Sale.total), func.count(models.Sale.id))\
        .filter(models.Sale.created_at >= start_of_day).first()
    sales_today = sales_today_query[0] or 0.0
    total_sales_count = sales_today_query[1] or 0
    average_ticket = sales_today / total_sales_count if total_sales_count > 0 else 0.0
    
    # 3. PPA (Peças Por Atendimento)
    items_sold_today = db.query(func.sum(models.SaleItem.quantity))\
        .join(models.Sale, models.SaleItem.sale_id == models.Sale.id)\
        .filter(models.Sale.created_at >= start_of_day).scalar() or 0
    ppa = items_sold_today / total_sales_count if total_sales_count > 0 else 0.0
    
    # 4. Margem Bruta (Estimada pelo custo atual dos produtos)
    # Nota: Em um ERP real, salvaríamos o cost_price_at_sale no SaleItem.
    gross_margin_data = db.query(
        func.sum(models.SaleItem.quantity * models.SaleItem.price_at_sale),
        func.sum(models.SaleItem.quantity * models.Product.cost_price)
    ).join(models.Product, models.SaleItem.product_id == models.Product.id)\
     .join(models.Sale, models.SaleItem.sale_id == models.Sale.id)\
     .filter(models.Sale.created_at >= start_of_day).first()
    
    revenue_today = gross_margin_data[0] or 0.0
    cost_today = gross_margin_data[1] or 0.0
    gross_margin_value = revenue_today - cost_today
    gross_margin_percent = (gross_margin_value / revenue_today * 100) if revenue_today > 0 else 0.0

    # 5. Mix de Categorias (Top 5)
    category_mix = db.query(
        models.Product.category,
        func.sum(models.SaleItem.quantity * models.SaleItem.price_at_sale).label("value")
    ).join(models.SaleItem, models.Product.id == models.SaleItem.product_id)\
     .join(models.Sale, models.SaleItem.sale_id == models.Sale.id)\
     .filter(models.Sale.created_at >= start_of_day)\
     .group_by(models.Product.category)\
     .order_by(func.sum(models.SaleItem.quantity * models.SaleItem.price_at_sale).desc())\
     .limit(5).all()
    
    category_data = [{"name": c[0], "value": c[1]} for c in category_mix]

    # 6. Alertas de Estoque (Real)
    low_stock_alerts = db.query(models.Product).filter(models.Product.status == "low_stock").count()

    # 7. Vendas Semanais
    weekly_sales = []
    for i in range(6, -1, -1):
        day = today - timedelta(days=i)
        day_start = datetime.combine(day, datetime.min.time())
        day_total = db.query(func.sum(models.Sale.total)).filter(models.Sale.created_at >= day_start, models.Sale.created_at <= datetime.combine(day, datetime.max.time())).scalar() or 0.0
        days_map = ["Seg", "Ter", "Qua", "Qui", "Sex", "Sáb", "Dom"]
        weekly_sales.append({
            "name": days_map[day.weekday()],
            "vendas": day_total,
            "pedidos": db.query(models.Sale).filter(models.Sale.created_at >= day_start, models.Sale.created_at <= datetime.combine(day, datetime.max.time())).count()
        })

    return {
        "total_customers": total_customers,
        "sales_today": sales_today,
        "low_stock_alerts": low_stock_alerts,
        "new_customers_today": new_customers_today,
        "average_ticket": average_ticket,
        "ppa": round(ppa, 2),
        "gross_margin_value": gross_margin_value,
        "gross_margin_percent": round(gross_margin_percent, 1),
        "category_data": category_data,
        "weekly_sales": weekly_sales
    }
