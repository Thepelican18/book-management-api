from typing import Optional, List

from domain.repositories.book_repository import BookRepository
from domain.models.book import Book
from domain.value_objects.isbn import ISBN
from domain.exceptions import BookNotFound, BookAlreadyExists


class BookService:
    def __init__(self, repository: BookRepository):
        self.repository = repository

    def create_book(self, title: str, author: str, publication_year: int, isbn: str, pages: int) -> Book:
        isbn: str = ISBN(isbn).value
        if self.repository.get(isbn) is not None:
            raise BookAlreadyExists(isbn)
        book = Book(title=title, author=author, publication_year=publication_year, isbn=isbn, pages=pages)
        self.repository.add(book)
        return book

    def get_book(self, isbn: str) -> Book:
        isbn: str  = ISBN(isbn).value
        book = self.repository.get(isbn)
        if not book:
            raise BookNotFound(f"Book with ISBN {isbn} not found")
        return book

    def update_book(self, isbn: str, title: str, author: str, publication_year: int, pages: int) -> Book:
        isbn: str  = ISBN(isbn).value
        book = self.get_book(isbn)
        book.title = title
        book.author = author
        book.publication_year = publication_year
        book.pages = pages
        self.repository.update(book)
        return book

    def delete_book(self, isbn: str) -> None:
        self.get_book(isbn) 
        self.repository.delete(isbn)

    def search_books(self, title: Optional[str] = None, author: Optional[str] = None) -> List[Book]:
        books = self.repository.search(title=title, author=author)
        if not books:
            raise BookNotFound("No books found with the given title or author")
        return books