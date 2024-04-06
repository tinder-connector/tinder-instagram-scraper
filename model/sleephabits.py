from sqlalchemy import Column, Integer, String
from model.base import Base

class SleepHabits(Base):
    __tablename__ = 'sleephabits'

    id = Column(Integer, primary_key=True)
    label = Column(String(255))