from sqlalchemy import Column, Integer, String, ForeignKey, BINARY
from model.base import Base

class Photo(Base):
    __tablename__ = 'photo'

    id = Column(Integer, primary_key=True)
    id_photo_tinder = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    crop_info = Column(String(1024))
    image = Column(BINARY)
    image_blurred = Column(BINARY)