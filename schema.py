from pydantic import BaseModel

class BookBase(BaseModel):
    title: str
    author: str
    description: str

    class Config:
        orm_mode = True

class Book(BookBase):
    id: int

class BookCreate(BookBase):
    pass

class BookUpdate(BookBase):
    pass