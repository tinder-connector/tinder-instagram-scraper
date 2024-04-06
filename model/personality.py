from sqlalchemy import Column, Integer, String
from model.base import Base

class Personality(Base):
    __tablename__ = 'personality'

    id = Column(Integer, primary_key=True)
    label = Column(String(255))