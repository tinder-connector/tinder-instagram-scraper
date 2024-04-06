from sqlalchemy import Column, Integer, String
from model.base import Base

class Badge(Base):
    __tablename__ = 'badge'

    id = Column(Integer, primary_key=True)
    label = Column(String(255))