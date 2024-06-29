from sqlalchemy import Column, String, Integer

from database import Base


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    description = Column(String, nullable=False)

