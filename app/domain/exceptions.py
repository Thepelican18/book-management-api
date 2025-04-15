class DomainError(Exception):
    """Base class"""
    pass

class InvalidISBNError(DomainError):
    pass

class InvalidTitleError(DomainError):
    pass

class InvalidAuthorError(DomainError):
    pass

class InvalidPublicationYearError(DomainError):
    pass

class InvalidPagesError(DomainError):
    pass

class BookNotFound(DomainError):
    pass
