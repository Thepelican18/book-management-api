import os
import pickle
from typing import Optional, List

from domain.repositories.book_repository  import BookRepository
from domain.models.book import Book

class PickleBookRepository(BookRepository):

    def __init__(self, file_path: str):
        self.file_path = file_path
      
        if os.path.exists(self.file_path):
            with open(self.file_path, 'rb') as f:
                self.books = pickle.load(f)
        else:
            self.books = {}

    def _save(self) -> None:
        with open(self.file_path, 'wb') as f:
            pickle.dump(self.books, f)

    def add(self, book: Book) -> None:
        self.books[book.isbn] = book
        self._save()

    def get(self, isbn: str) -> Book:
        return self.books.get(isbn)

    def update(self, book: Book) -> None:
        if book.isbn in self.books:
            self.books[book.isbn] = book
            self._save()

    def delete(self, isbn: str) -> None:
        if isbn in self.books:
            del self.books[isbn]
            self._save()

    def search(self, title: Optional[str] = None, author: Optional[str] = None) -> List[Book]:
        books = self.books.values()
        if title:
            results = [book for book in books if title.lower() in book.title.lower()]
        if author:
            results = [book for book in books if author.lower() in book.author.lower()]
        return results
    
