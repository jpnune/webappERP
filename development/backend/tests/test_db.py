import sys
# Hack para garantir o driver sqlcipher
try:
    import sqlcipher3
    sys.modules['pysqlcipher3'] = sqlcipher3
except ImportError:
    pass

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Base
from models import Product, Customer

TEST_DB_URL = "sqlite+pysqlcipher://:test_secret@/:memory:"
engine = create_engine(TEST_DB_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def setup_module(module):
    Base.metadata.create_all(bind=engine)

def teardown_module(module):
    Base.metadata.drop_all(bind=engine)

def test_create_and_read_product():
    db = TestingSessionLocal()
    
    new_product = Product(
        name="Vestido Infantil Teste",
        sku="VEST-TST-01",
        barcode="1234567890",
        cost_price=25.0,
        selling_price=50.0,
        margin=100.0,
        variants_json='[{"size":"M","color":"Red","stock":10}]'
    )
    
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    
    assert new_product.id is not None
    assert new_product.name == "Vestido Infantil Teste"
    
    # Read
    product = db.query(Product).filter(Product.sku == "VEST-TST-01").first()
    assert product is not None
    assert product.cost_price == 25.0

    db.close()

def test_create_customer():
    db = TestingSessionLocal()
    
    customer = Customer(
        first_name="João",
        last_name="Silva",
        email="joao@teste.com",
        phone="(11) 99999-9999",
        cpf="00011122233"
    )
    
    db.add(customer)
    db.commit()
    db.refresh(customer)
    
    assert customer.id is not None
    assert customer.first_name == "João"
    
    db.close()
