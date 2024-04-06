from sqlalchemy import Column, Integer, String
from model.base import Base

class SmokingFrequency(Base):
    __tablename__ = 'smokingfrequency'

    id = Column(Integer, primary_key=True)
    label = Column(String(255))