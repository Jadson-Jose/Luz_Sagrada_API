from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.crud.book import create_book, get_books
from app.database import get_db
from app.schemas.book import Book, BookCreate

router = APIRouter()


@router.post("/books/", response_model=Book)
def create_book_route(book: BookCreate, db: Session = Depends(get_db)):
    return create_book(db=db, book=book)


@router.get("/books/", response_model=list[Book])
def read_books(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_books(db=db, skip=skip, limit=limit)
