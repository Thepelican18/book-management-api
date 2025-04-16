import pytest
import sys
import os


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))

from application.services.book_service import BookService
from infrastructure.repositories.pickle_book_repository import PickleBookRepository
from config import PathConfig
from domain.models.book import Book
from domain.exceptions import BookNotFound


@pytest.fixture(autouse=True)
def clear_pickle_db():
    if os.path.exists(PathConfig.PICKLE_PATH):
        os.remove(PathConfig.PICKLE_PATH)

@pytest.fixture
def book_service():
        return BookService(repository=PickleBookRepository(file_path=PathConfig.PICKLE_PATH))


@pytest.fixture
def book():
    return Book(
        title="1984",
        author="George Orwell2",
        publication_year=1949,
        isbn="278-0-452-38423-4",
        pages=328
    )

def test_create_book(book_service, book):
    created_book = book_service.create_book(
        title=book.title,
        author=book.author,
        publication_year=book.publication_year,
        isbn=book.isbn,
        pages=book.pages
    )
    assert created_book.title == book.title
    assert created_book.isbn == book.isbn

def test_get_book(book_service, book):
    book_service.create_book(
        title=book.title,
        author=book.author,
        publication_year=book.publication_year,
        isbn=book.isbn,
        pages=book.pages
    )
    retrieved_book = book_service.get_book(book.isbn)
    assert retrieved_book.isbn == book.isbn

def test_update_book(book_service, book):
    book_service.create_book(
        title=book.title,
        author=book.author,
        publication_year=book.publication_year,
        isbn=book.isbn,
        pages=book.pages
    )
    updated_book = book_service.update_book(
        isbn=book.isbn,
        title="1984 (Updated)",
        author=book.author,
        publication_year=book.publication_year,
        pages=book.pages
    )
    assert updated_book.title == "1984 (Updated)"

def test_delete_book(book_service, book):
    book_service.create_book(
        title=book.title,
        author=book.author,
        publication_year=book.publication_year,
        isbn=book.isbn,
        pages=book.pages
    )
    book_service.delete_book(book.isbn)
    with pytest.raises(BookNotFound):
        book_service.get_book(book.isbn)

def test_search_books(book_service):
   
    book1 = book_service.create_book(
        title="1984",
        author="George Orwell",
        publication_year=1949,
        isbn="978-0-452-28423-4",
        pages=328
    )
    book2 = book_service.create_book(
        title="Animal Farm",
        author="George Orwell",
        publication_year=1945,
        isbn="978-0-452-28423-5",
        pages=112
    )
    
    results_by_author = book_service.search_books(title=None, author="Orwell")
    assert isinstance(results_by_author, list)
    assert len(results_by_author) == 2
    
    for b in results_by_author:
        assert "orwell" in b.author.lower()
    
    
    results_by_title = book_service.search_books(title="1984", author=None)
    assert isinstance(results_by_title, list)
    assert len(results_by_title) == 1
    assert results_by_title[0].isbn == book1.isbn

    with pytest.raises(BookNotFound):
        book_service.search_books(title="Nonexistent", author="No one")


