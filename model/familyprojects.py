from sqlalchemy import Column, Integer, String
from model.base import Base

class FamilyProjects(Base):
    __tablename__ = 'familyprojects'

    id = Column(Integer, primary_key=True)
    label = Column(String(255))