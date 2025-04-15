from domain.exceptions import InvalidTitleError, InvalidAuthorError, InvalidPublicationYearError, InvalidPagesError
from domain.value_objects.isbn import ISBN

class Book:
    def __init__(self, isbn: ISBN, title: str, author: str, publication_year: int, pages: int):
        self._validate(isbn, title, author, publication_year, pages)

        self.isbn = isbn
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.pages = pages

    def _validate(self, title, author, publication_year, pages):
        if not title:
            raise InvalidTitleError("Title must not be empty.")
        if not author:
            raise InvalidAuthorError("Author must not be empty.")
        if publication_year < 0:
            raise InvalidPublicationYearError("Publication year must be a positive integer.")
        if pages <= 0:
            raise InvalidPagesError("Pages must be a positive number.")


