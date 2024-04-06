from sqlalchemy import Column, Integer, String
from model.base import Base

class SocialNetworks(Base):
    __tablename__ = 'socialnetworks'

    id = Column(Integer, primary_key=True)
    label = Column(String(255))