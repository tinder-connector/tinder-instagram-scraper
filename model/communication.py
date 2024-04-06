from sqlalchemy import Column, Integer, String
from model.base import Base

class Communication(Base):
    __tablename__ = 'communication'

    id = Column(Integer, primary_key=True)
    label = Column(String(255))