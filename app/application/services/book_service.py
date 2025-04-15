from domain.repositories.book_repository import BookRepository
from domain.models.book import Book
from domain.exceptions import BookNotFound, BookAlreadyExists


class BookService:
    def __init__(self, repository: BookRepository):
        self.repository = repository

    def create_book(self, title: str, author: str, publication_year: int, isbn: str, pages: int) -> Book:
        if self.repository.get(isbn) is not None:
            raise BookAlreadyExists(isbn)
        book = Book(title=title, author=author, publication_year=publication_year, isbn=isbn, pages=pages)
        self.repository.add(book)
        return book

    def get_book(self, isbn: str) -> Book:
        book = self.repository.get(isbn)
        if not book:
            raise BookNotFound(isbn)
        return book

    def update_book(self, isbn: str, title: str, author: str, publication_year: int, pages: int) -> Book:
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