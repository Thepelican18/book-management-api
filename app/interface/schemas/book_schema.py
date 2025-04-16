from pydantic import BaseModel

class CreateBook(BaseModel):
    title: str
    author: str
    publication_year: int
    isbn: str
    pages: int

class GetBook(BaseModel):
    title: str
    author: str
    publication_year: int
    isbn: str
    pages: int

class UpdateBook(BaseModel):
    title: str
    author: str
    publication_year: int
    pages: int

  
