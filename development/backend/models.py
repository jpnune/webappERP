from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base

class Category(Base):
    __tablename__ = "categories"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)

class Customer(Base):
    __tablename__ = "customers"
    
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String)
    email = Column(String, unique=True, index=True)
    phone = Column(String)
    cpf = Column(String, unique=True, index=True)
    
    address = Column(String)
    number = Column(String)
    neighborhood = Column(String)
    complement = Column(String)
    city = Column(String)
    state = Column(String)
    cep = Column(String)
    
    loyalty_level = Column(String, default="bronze")
    points = Column(Integer, default=0)
    
    created_at = Column(DateTime, default=datetime.utcnow)
    status = Column(String, default="Ativo")
    notes = Column(String, default="")
    
    # Sistema de Crédito
    credit_enabled = Column(Boolean, default=False)
    credit_limit_rate = Column(Float, default=0.0)
    manual_credit_limit = Column(Float, default=0.0)
    
    sales = relationship("Sale", back_populates="customer")

class Product(Base):
    __tablename__ = "products"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    sku = Column(String, unique=True, index=True)
    barcode = Column(String, unique=True, index=True)
    category = Column(String)
    brand = Column(String)
    supplier = Column(String)
    min_stock = Column(Integer, default=5)
    
    cost_price = Column(Float)
    selling_price = Column(Float)
    margin = Column(Float)
    
    # Campo JSON embutido via String para matriz simples de Mocks
    variants_json = Column(String) 
    
    status = Column(String, default="in_stock")
    created_at = Column(DateTime, default=datetime.utcnow)

class Sale(Base):
    __tablename__ = "sales"
    
    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=True)
    total = Column(Float)
    discount = Column(Float, default=0.0)
    payment_method = Column(String) # credit_card, cash, pix
    status = Column(String, default="completed")
    created_at = Column(DateTime, default=datetime.utcnow)
    
    customer = relationship("Customer", back_populates="sales")
    items = relationship("SaleItem", back_populates="sale")

class SaleItem(Base):
    __tablename__ = "sale_items"
    
    id = Column(Integer, primary_key=True, index=True)
    sale_id = Column(Integer, ForeignKey("sales.id"))
    product_id = Column(Integer, ForeignKey("products.id"))
    quantity = Column(Integer)
    price_at_sale = Column(Float)
    color = Column(String, nullable=True)
    size = Column(String, nullable=True)
    
    sale = relationship("Sale", back_populates="items")
    product = relationship("Product")

class Employee(Base):
    __tablename__ = "employees"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    role = Column(String)
    department = Column(String)
    contact = Column(String)
    cpf = Column(String)
    date_hired = Column(String)
    status = Column(String, default="Ativo")
    created_at = Column(DateTime, default=datetime.utcnow)

class Vendor(Base):
    __tablename__ = "vendors"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    contact_person = Column(String)
    phone = Column(String)
    cpf_cnpj = Column(String)
    instagram = Column(String)
    website = Column(String)
    secondary_phones = Column(String) # JSON com [{ "phone": "...", "label": "..." }]
    zip_code = Column(String)
    street = Column(String)
    number = Column(String)
    complement = Column(String)
    neighborhood = Column(String)
    city = Column(String)
    state = Column(String)
    products_count = Column(Integer, default=0)
    rating = Column(Float, default=5.0)
    total_value = Column(Float, default=0.0)
    status = Column(String, default="Ativo")
    created_at = Column(DateTime, default=datetime.utcnow)

class PurchaseInvoice(Base):
    __tablename__ = "purchase_invoices"
    
    id = Column(Integer, primary_key=True, index=True)
    invoice_number = Column(String, index=True)
    vendor_id = Column(Integer, ForeignKey("vendors.id"))
    purchase_date = Column(DateTime)
    entry_date = Column(DateTime, default=datetime.utcnow)
    total_amount = Column(Float)
    shipping_cost = Column(Float, default=0.0)
    status = Column(String, default="completed") # draft, completed
    notes = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    vendor = relationship("Vendor")
    items = relationship("PurchaseItem", back_populates="invoice")

class PurchaseItem(Base):
    __tablename__ = "purchase_items"
    
    id = Column(Integer, primary_key=True, index=True)
    invoice_id = Column(Integer, ForeignKey("purchase_invoices.id"))
    product_id = Column(Integer, ForeignKey("products.id"))
    quantity = Column(Integer)
    cost_price = Column(Float)
    color = Column(String, nullable=True)
    size = Column(String, nullable=True)
    
    invoice = relationship("PurchaseInvoice", back_populates="items")
    product = relationship("Product")
