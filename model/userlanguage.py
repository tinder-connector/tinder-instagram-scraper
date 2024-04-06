from sqlalchemy import Column, Integer, ForeignKey
from model.base import Base

class UserLanguage(Base):
    __tablename__ = 'userlanguage'

    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    language_id = Column(Integer, ForeignKey('language.id'), primary_key=True)