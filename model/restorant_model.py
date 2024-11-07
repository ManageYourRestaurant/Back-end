import uuid
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from config.db_config import Base


class RestorantModel(Base):
    __tablename__ = "restorant"
    restorant_id: Mapped[str] = mapped_column(String, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String)
