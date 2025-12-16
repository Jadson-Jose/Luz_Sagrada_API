from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from app.database import Base


class Chapter(Base):
    __tablename__ = "chapters"
    id = Column(Integer, primary_key=True, index=True)
    number = Column(Integer, index=True)
    book_id = Column(Integer, ForeignKey("books.id"))

    book = relationship("Book", back_populates="chapters")
    verses = relationship("Verse", back_populates="chapter")
