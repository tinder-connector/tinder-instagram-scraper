from sqlalchemy import Column, Integer, String
from model.base import Base

class Alcohol(Base):
    __tablename__ = 'alcohol'

    id = Column(Integer, primary_key=True)
    label = Column(String(255))