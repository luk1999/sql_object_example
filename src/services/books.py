from sqlobject import SQLObjectNotFound

from entities import BaseBook, BaseBookWithAuthor
from errors import DoesNotExistError
from models import Book


class BookService:
    @staticmethod
    def get_all() -> tuple[BaseBook]:
        return tuple(map(BaseBook.from_orm, Book.select()))

    @staticmethod
    def get(book_id: int) -> BaseBookWithAuthor:
        try:
            book = Book.get(book_id)
            return BaseBookWithAuthor.from_orm(book)
        except SQLObjectNotFound:
            raise DoesNotExistError
