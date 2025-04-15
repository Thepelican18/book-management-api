class DomainError(Exception):
    def __init__(self, detail: str):
        self.detail = detail
        super().__init__(self.detail)

class InvalidTitleError(DomainError):
    pass

class InvalidAuthorError(DomainError):
    pass

class InvalidPublicationYearError(DomainError):
    pass

class InvalidPagesError(DomainError):
    pass

class InvalidBookData(DomainError):
    pass

class InvalidISBNError(DomainError):
    def __init__(self):
        self.detail = f"ISBN must follow the format '978-0-452-28423-4'."
        super().__init__(self.detail)

class BookNotFound(DomainError):
    def __init__(self, isbn: str):
        self.detail = f"Book with ISBN {isbn} not found"
        super().__init__(self.detail)

class BookAlreadyExists(DomainError):
    def __init__(self, isbn: str):
        self.detail = f"A book with ISBN {isbn} already exists."
        super().__init__(self.detail)
