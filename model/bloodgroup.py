from sqlalchemy import Column, Integer, String
from model.base import Base

class BloodGroup(Base):
    __tablename__ = 'bloodgroup'

    id = Column(Integer, primary_key=True)
    label = Column(String(255))