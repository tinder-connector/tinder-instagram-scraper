from sqlalchemy import Column, Integer, String
from model.base import Base

class LevelStudy(Base):
    __tablename__ = 'levelstudy'

    id = Column(Integer, primary_key=True)
    label = Column(String(255))