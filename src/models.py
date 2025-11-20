from sqlobject import (
    DatabaseIndex,
    DateCol,
    EnumCol,
    ForeignKey,
    IntCol,
    MultipleJoin,
    RelatedJoin,
    SQLObject,
    StringCol,
    connectionForURI,
    sqlhub,
)
from sqlobject.manager.command import SQLObjectVersionTable

import config
from enums import GENRES, UserStatus, USER_STATUSES


def get_connection():
    return connectionForURI(config.DATABASE_CONNECTION_STR)


sqlhub.processConnection = get_connection()


class Author(SQLObject):
    first_name = StringCol(length=100, notNone=True)
    last_name = StringCol(length=100, notNone=True)
    date_of_birth = DateCol(notNone=True)

    books = MultipleJoin("Book")

    indexes = [
        DatabaseIndex("first_name", "last_name", "date_of_birth", unique=True),
    ]


class Book(SQLObject):
    author = ForeignKey("Author", notNone=True)
    title = StringCol(length=100, notNone=True)
    year = IntCol(notNone=True)
    genre = EnumCol(enumValues=GENRES, notNone=True)
    # New col
    rate = IntCol(notNone=False)

    users = RelatedJoin("User")

    indexes = [
        DatabaseIndex("author", "title", unique=True),
    ]


class User(SQLObject):
    username = StringCol(length=50, unique=True, notNone=True)
    password = StringCol(length=32, notNone=False)
    first_name = StringCol(length=100, notNone=False, default=None)
    last_name = StringCol(length=100, notNone=False, default=None)
    status = EnumCol(enumValues=USER_STATUSES, notNone=True, default=UserStatus.inactive.value)

    books = RelatedJoin("Book")


Author.createTable(ifNotExists=True)
Book.createTable(ifNotExists=True)
User.createTable(ifNotExists=True)

SQLObjectVersionTable.createTable(ifNotExists=True)
