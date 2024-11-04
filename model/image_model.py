from sqlalchemy import Column, String
from config.db_config import Base


class ImageModel(Base):
    __tablename__ = "image"
    image_id = Column(String, unique=True)
    content = Column(String)
