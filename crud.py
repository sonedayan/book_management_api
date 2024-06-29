from sqlalchemy.orm import Session
import models
import schema
from fastapi.encoders import jsonable_encoder

def get_book(db: Session, id: int):
    return db.query(models.Book).filter(models.Book.id == id).first()

def get_book_by_author(db: Session, author: str):
    return db.query(models.Book).filter(models.Book.author == author).first()

def get_books(db: Session, offset: int = 0, limit: int = 10):
    return db.query(models.Book).all()

def create_book(db: Session, book: schema.BookCreate):
    db_book = models.Book(**book.model_dump())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def update_book(db: Session, book_id: int, book_payload: schema.BookUpdate):
    book = get_book(db, book_id)
    if not book:
        return None
    
    book_payload_dict = book_payload.dict(exclude_unset=True)

    for k, v in book_payload_dict.items():
        setattr(book, k, v)

    # book.title = book_payload.title
    # book.author = book_payload.author
    # book.description = book_payload.description
    db.add(book)
    db.commit()
    db.refresh(book)

    return book

