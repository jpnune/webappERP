from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class CategoryBase(BaseModel):
    name: str

class CategoryCreate(CategoryBase):
    pass

class CategorySchema(CategoryBase):
    id: int
    created_at: datetime
    class Config:
        from_attributes = True

# --- CUSTOMER SCHEMAS ---
class CustomerBase(BaseModel):
    first_name: str
    last_name: Optional[str] = None
    email: Optional[str] = None
    phone: str
    cpf: Optional[str] = None
    address: Optional[str] = None
    number: Optional[str] = None
    neighborhood: Optional[str] = None
    complement: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    cep: Optional[str] = None
    loyalty_level: Optional[str] = "bronze"
    points: Optional[int] = 0
    status: Optional[str] = "Ativo"
    notes: Optional[str] = None
    credit_enabled: Optional[bool] = False
    credit_limit_rate: Optional[float] = 0.0
    manual_credit_limit: Optional[float] = 0.0

class CustomerCreate(CustomerBase):
    pass

class CustomerUpdate(CustomerBase):
    pass

class CustomerSchema(CustomerBase):
    id: int
    created_at: datetime
    total_spent: float = 0.0
    calculated_credit_limit: float = 0.0
    credit_used: float = 0.0
    class Config:
        from_attributes = True

# --- PRODUCT SCHEMAS ---
class ProductBase(BaseModel):
    name: str
    sku: Optional[str] = ""
    barcode: Optional[str] = ""
    category: str
    brand: Optional[str] = "Genérica"
    supplier: Optional[str] = "Fornecedor Local"
    min_stock: Optional[int] = 5
    cost_price: Optional[float] = 0.0
    selling_price: Optional[float] = 0.0
    margin: Optional[float] = 0.0
    variants_json: str
    status: Optional[str] = "Ativo"

class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductBase):
    pass

class ProductSchema(ProductBase):
    id: int
    created_at: datetime
    class Config:
        from_attributes = True

# --- SALES SCHEMAS ---

class SaleItemBase(BaseModel):
    product_id: int
    quantity: int
    price_at_sale: float
    color: Optional[str] = None
    size: Optional[str] = None

class SaleItemCreate(SaleItemBase):
    pass

class SaleItem(SaleItemBase):
    id: int
    sale_id: int
    class Config:
        from_attributes = True

class SaleBase(BaseModel):
    customer_id: Optional[int] = None
    total: float
    discount: float = 0.0
    payment_method: str

class SaleCreate(SaleBase):
    items: List[SaleItemCreate]

class Sale(SaleBase):
    id: int
    status: str
    created_at: datetime
    items: List[SaleItem] = []
    class Config:
        from_attributes = True

# --- STAFF SCHEMAS ---
class EmployeeBase(BaseModel):
    name: str
    role: str
    department: str
    contact: str
    cpf: Optional[str] = None
    date_hired: str
    status: Optional[str] = "Ativo"

class EmployeeCreate(EmployeeBase):
    pass

class EmployeeUpdate(BaseModel):
    name: Optional[str] = None
    role: Optional[str] = None
    department: Optional[str] = None
    contact: Optional[str] = None
    cpf: Optional[str] = None
    date_hired: Optional[str] = None
    status: Optional[str] = None

class EmployeeSchema(EmployeeBase):
    id: int
    created_at: datetime
    class Config:
        from_attributes = True

# --- VENDOR SCHEMAS ---
class VendorBase(BaseModel):
    name: str
    contact_person: str
    phone: str
    cpf_cnpj: Optional[str] = None
    instagram: Optional[str] = None
    website: Optional[str] = None
    secondary_phones: Optional[str] = None
    zip_code: Optional[str] = None
    street: Optional[str] = None
    number: Optional[str] = None
    complement: Optional[str] = None
    neighborhood: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    products_count: Optional[int] = 0
    rating: Optional[float] = 5.0
    total_value: Optional[float] = 0.0
    status: Optional[str] = "Ativo"

class VendorCreate(VendorBase):
    pass

class VendorSchema(VendorBase):
    id: int
    created_at: datetime
    class Config:
        from_attributes = True

# --- PURCHASE (ENTRIES) SCHEMAS ---
class PurchaseItemBase(BaseModel):
    product_id: int
    quantity: int
    cost_price: float
    color: Optional[str] = None
    size: Optional[str] = None

class PurchaseItemCreate(PurchaseItemBase):
    pass

class PurchaseItemSchema(PurchaseItemBase):
    id: int
    invoice_id: int
    class Config:
        from_attributes = True

class PurchaseInvoiceBase(BaseModel):
    invoice_number: str
    vendor_id: int
    purchase_date: datetime
    total_amount: float
    shipping_cost: float = 0.0
    notes: Optional[str] = None

class PurchaseInvoiceCreate(PurchaseInvoiceBase):
    items: List[PurchaseItemCreate]

class PurchaseInvoiceSchema(PurchaseInvoiceBase):
    id: int
    entry_date: datetime
    status: str
    created_at: datetime
    items: List[PurchaseItemSchema] = []
    class Config:
        from_attributes = True
