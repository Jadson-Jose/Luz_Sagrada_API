from pydantic import BaseModel


class BookBase(BaseModel):
    name: str
    abbreviation: str


class BookCreate(BookBase):
    pass


class Book(BookBase):
    id: int

    class Config:
        orm_mode = True
