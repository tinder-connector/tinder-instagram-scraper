from sqlalchemy import Column, Integer, String
from model.base import Base

class SexualOrientation(Base):
    __tablename__ = 'sexualorientation'

    id = Column(Integer, primary_key=True)
    code = Column(String(10))
    label = Column(String(255))
    description = Column(String(255))