from sqlalchemy import Column, Integer, String
from model.base import Base

class Sport(Base):
    __tablename__ = 'sport'

    id = Column(Integer, primary_key=True)
    label = Column(String(255))