from sqlalchemy import Column, String
from config.db_config import Base


class CommentModel(Base):
    __tablename__ = "comment"
    comment_id = Column(String, unique=True)
    content = Column(String)

    image = ""
