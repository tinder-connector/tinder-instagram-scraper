from sqlalchemy import Column, Integer, String
from model.base import Base

class School(Base):
    __tablename__ = 'school'

    id = Column(Integer, primary_key=True)
    label = Column(String(255))