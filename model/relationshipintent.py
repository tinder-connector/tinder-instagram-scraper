from sqlalchemy import Column, Integer, String
from model.base import Base

class RelationshipIntent(Base):
    __tablename__ = 'relationshipintent'

    id = Column(Integer, primary_key=True)
    label = Column(String(255))