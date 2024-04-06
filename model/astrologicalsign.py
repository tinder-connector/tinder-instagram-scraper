from sqlalchemy import Column, Integer, String
from model.base import Base

class AstrologicalSign(Base):
    __tablename__ = 'astrologicalsign'

    id = Column(Integer, primary_key=True)
    label = Column(String(255))