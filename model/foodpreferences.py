from sqlalchemy import Column, Integer, String
from model.base import Base

class FoodPreferences(Base):
    __tablename__ = 'foodpreferences'

    id = Column(Integer, primary_key=True)
    label = Column(String(255))