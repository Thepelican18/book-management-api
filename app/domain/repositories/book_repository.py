from abc import ABC, abstractmethod
from domain.models.book import Book

class BookRepository(ABC):
    @abstractmethod
    def add(self, book: Book) -> None:
        pass

    @abstractmethod
    def get(self, isbn: str) -> Book:
        pass

    @abstractmethod
    def update(self, book: Book) -> None:
        pass

    @abstractmethod
    def delete(self, isbn: str) -> None:
        pass
