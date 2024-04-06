from sqlalchemy import Column, Integer, ForeignKey
from model.base import Base

class UserBadge(Base):
    __tablename__ = 'userbadge'

    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    badge_id = Column(Integer, ForeignKey('badge.id'), primary_key=True)