from sqlobject import SQLObjectNotFound

from entities import BaseAuthor, BaseAuthorWithBooks
from errors import DoesNotExistError
from models import Author


class AuthorService:
    @staticmethod
    def get_all() -> tuple[BaseAuthor]:
        return tuple(map(BaseAuthor.from_orm, Author.select()))

    @staticmethod
    def get(author_id: int) -> BaseAuthorWithBooks:
        try:
            author = Author.get(author_id)
            return BaseAuthorWithBooks.from_orm(author)
        except SQLObjectNotFound:
            raise DoesNotExistError
