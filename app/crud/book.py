from sqlalchemy.orm import Session

from app.models.book import Book
from app.schemas.book import BookCreate


def create_book(db: Session, book: BookCreate):
    db_book = Book(name=book.name, abbreviation=book.abbreviation)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


def get_books(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Book).offset(skip).limit(limit).all()
