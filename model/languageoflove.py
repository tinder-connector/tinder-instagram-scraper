from sqlalchemy import Column, Integer, String
from model.base import Base

class LanguageOfLove(Base):
    __tablename__ = 'languageoflove'

    id = Column(Integer, primary_key=True)
    label = Column(String(255))