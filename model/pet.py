from sqlalchemy import Column, Integer, String
from model.base import Base

class Pet(Base):
    __tablename__ = 'pet'

    id = Column(Integer, primary_key=True)
    label = Column(String(255))