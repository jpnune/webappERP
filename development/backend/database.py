import sys
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Configuração para o SQLAlchemy reconhecer a lib sqlcipher3 instalada
try:
    import sqlcipher3
    sys.modules['pysqlcipher3'] = sqlcipher3
except ImportError:
    print("Aviso: sqlcipher3 não encontrado no ambiente.")

DB_PASSWORD = os.getenv("DB_PASSWORD", "LolliPopSuperSecretKey2026!")
# Em ambiente de desenvolvimento, o arquivo será gerado na pasta do backend
SQLALCHEMY_DATABASE_URL = f"sqlite+pysqlcipher://:{DB_PASSWORD}@/lollipop_local.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, 
    connect_args={"check_same_thread": False} # Importante em FastAPI e SQLite local
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependência do FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
