from fastapi.testclient import TestClient
from main import app
from database import Base, engine

client = TestClient(app)

# Executa antes para ter certeza que as tabelas existem
Base.metadata.create_all(bind=engine)

def test_create_customer():
    response = client.post(
        "/customers/",
        json={
            "first_name": "Maria",
            "last_name": "Jose",
            "email": "maria@teste.com",
            "phone": "(11) 98888-8888",
            "cpf": "12345678901",
            "address": "Rua A",
            "number": "100",
            "neighborhood": "Centro",
            "city": "SP",
            "state": "SP"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["first_name"] == "Maria"
    assert "id" in data

def test_read_customers():
    response = client.get("/customers/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0
    assert data[0]["first_name"] == "Maria"

def test_create_product():
    response = client.post(
        "/products/",
        json={
            "name": "Camiseta API Teste",
            "sku": "CAM-API-01",
            "barcode": "00000000000",
            "category": "Roupas",
            "brand": "LolliPop",
            "supplier": "Fornecedor X",
            "min_stock": 5,
            "cost_price": 20.0,
            "selling_price": 40.0,
            "margin": 100.0,
            "variants_json": "[]",
            "status": "in_stock"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Camiseta API Teste"
    assert "id" in data
