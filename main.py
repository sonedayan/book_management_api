from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import crud, schema
from database import SessionLocal, engine, Base
from typing import Optional

Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/books/")
def get_books(db: Session = Depends(get_db), offset: int = 0, limit: int = 10):
    books = crud.get_books(db, offset=offset, limit=limit)
    return {'message': 'success', 'data': books}

@app.get("/book/", response_model=schema.Book)
def get_book(book_id: str, db: Session = Depends(get_db)):
    book = crud.get_book(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@app.post('/books')
def create_book(payload: schema.BookCreate, db: Session = Depends(get_db)):
    crud.create_book(db, payload)
    return {'message': 'success'}

@app.put('/books/{book_id}')
def update_book(book_id: int, payload: schema.BookUpdate, db: Session = Depends(get_db)):
    book = crud.update_book(db, book_id, payload)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return {'message': 'success', 'data': book}