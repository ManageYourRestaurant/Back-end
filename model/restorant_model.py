from sqlalchemy import Column, String
from config.db_config import Base


class RestorantModel(Base):
    __tablename__ = "restorant"
    restorant_id = Column(String, unique=True)
    tag = Column(String)

    comment = ""
