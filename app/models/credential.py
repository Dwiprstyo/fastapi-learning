from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class Credential(Base):
    __tablename__ = "cnt_payment_credential"
    id: int = Column(Integer, primary_key=True, index=True)
    vendor: str = Column(String(50), index=True)
    company_code: str = Column(String(50), unique=True, index=True)
    credential_sand: str = Column()
    credential_prod: str = Column()