from sqlalchemy import Column, Integer, String
from model.base import Base

class Job(Base):
    __tablename__ = 'job'

    id = Column(Integer, primary_key=True)
    company = Column(String(255))
    profession = Column(String(255))