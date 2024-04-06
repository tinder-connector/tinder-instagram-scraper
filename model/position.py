from sqlalchemy import Column, Integer, DECIMAL
from model.base import Base

class Position(Base):
    __tablename__ = 'position'

    id = Column(Integer, primary_key=True)
    latitude = Column(DECIMAL(30,0), nullable=False)
    longitude = Column(DECIMAL(30,0), nullable=False)