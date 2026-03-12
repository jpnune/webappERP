from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine, Base
from routers import customers, products, sales, categories, staff, vendors, dashboard, reports, purchases

# Garante que as tabelas sejam criadas no SQLite criptografado
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="LolliPop ERP API",
    description="Backend offline local-first para o LolliPop ERP",
    version="1.0.0"
)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registrar Rotas
app.include_router(customers.router)
app.include_router(products.router)
app.include_router(sales.router)
app.include_router(categories.router)
app.include_router(staff.router)
app.include_router(vendors.router)
app.include_router(dashboard.router)
app.include_router(reports.router)
app.include_router(purchases.router)

@app.get("/")
async def root():
    return {"message": "Bem-vindo à API do LolliPop ERP"}

@app.get("/health")
async def health_check():
    return {"status": "ok"}
