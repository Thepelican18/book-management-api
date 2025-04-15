import re
from domain.exceptions import InvalidISBNError

class ISBN:
    def __init__(self, value: str):

        if not self._is_valid_format(value):
            raise InvalidISBNError()
        self._value = value

    def _is_valid_format(self, value: str) -> bool:
        isbn_pattern = r"^\d{3}-\d{1}-\d{3}-\d{5}-\d{1}$"
        return bool(re.match(isbn_pattern, value))

    @property
    def value(self) -> str:
        return self._value

    def __eq__(self, other):
        if isinstance(other, ISBN):
            return self._value == other._value
        return False

    def __hash__(self):
        return hash(self._value)

    def __str__(self):
        return self._value
