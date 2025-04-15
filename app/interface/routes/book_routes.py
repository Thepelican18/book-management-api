from fastapi import APIRouter

from application.services.book_service import BookService
from config import PathConfig
from infrastructure.repositories.pickle_book_repository import PickleBookRepository
from interface.schemas.book_schema import CreateBook,GetBook, UpdateBook, DeleteBook

book_router = APIRouter(prefix="/books")

@book_router.post("/", response_model=GetBook)
async def create_book(book: CreateBook):
    book_service = BookService(repository=PickleBookRepository(file_path=PathConfig.PICKLE_PATH))
    book_domain = book_service.create_book(
        title=book.title,
        author=book.author,
        publication_year=book.publication_year,
        isbn=book.isbn,
        pages=book.pages
    )
    return book_domain

@book_router.get("/{isbn}", response_model=GetBook)
async def get_book(isbn: str):
    book_service = BookService(repository=PickleBookRepository(file_path=PathConfig.PICKLE_PATH))
    book = book_service.get_book(isbn)
    return book

@book_router.put("/{isbn}", response_model=GetBook)
async def update_book(isbn: str, book: UpdateBook):
    book_service = BookService(repository=PickleBookRepository(file_path=PathConfig.PICKLE_PATH))
    updated_book = book_service.update_book(
        isbn=isbn,
        title=book.title,
        author=book.author,
        publication_year=book.publication_year,
        pages=book.pages
    )
    return updated_book

@book_router.delete("/")
async def delete_book(book: DeleteBook):
    book_service = BookService(repository=PickleBookRepository(file_path=PathConfig.PICKLE_PATH))
    book_service.delete_book(book.isbn)
    return {"message": f"Book with ISBN {book.isbn} has been deleted"}
