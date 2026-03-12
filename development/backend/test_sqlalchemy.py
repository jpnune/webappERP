from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, Integer, String

try:
    import sqlcipher3
    import sys
    sys.modules['pysqlcipher3'] = sqlcipher3
except ImportError:
    pass

engine = create_engine("sqlite+pysqlcipher://:segredo_forte@/:memory:")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class TestUser(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

Base.metadata.create_all(bind=engine)

db = SessionLocal()
db.add(TestUser(name="Admin SQLCipher"))
db.commit()

user = db.query(TestUser).first()
print(f"Sucesso ao ler do banco criptografado! User: {user.name}")
