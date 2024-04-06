from sqlalchemy import Column, Integer, String
from model.base import Base

class Language(Base):
    __tablename__ = 'language'

    id = Column(Integer, primary_key=True)
    label = Column(String(255))