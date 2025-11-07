from datetime import date

from enums import Genre, UserStatus
from models import Author, Book, User
from services.users import UserService


def init_data():
    clarke = Author(first_name="Arthur Charles", last_name="Clarke", date_of_birth=date(1917, 12, 16))
    king = Author(first_name="Stephen", last_name="King", date_of_birth=date(1947, 9, 21))
    grisham = Author(first_name="John", last_name="Grisham", date_of_birth=date(1955, 2, 8))

    Book(author=clarke, title="2001: A Space Odyssey", year=1968, genre=Genre.sci_fi.value)
    Book(author=king, title="It", year=1986, genre=Genre.horror.value)
    Book(author=king, title="The Shining", year=1977, genre=Genre.horror.value)
    gunslinger = Book(author=king, title="The Gunslinger", year=1982, genre=Genre.fantasy.value)
    pelican = Book(author=grisham, title="The Pelican Brief", year=1992, genre=Genre.thriller.value)
    rainmaker = Book(author=grisham, title="The Rainmaker", year=1995, genre=Genre.thriller.value)

    smith = User(
        username="john_smith",
        password=UserService.encode_password("12345678"),
        first_name="John",
        last_name="Smith",
        status=UserStatus.active.value,
    )
    smith.addBook(rainmaker)
    smith.addBook(gunslinger)

    rambo = User(
        username="rambo",
        password=UserService.encode_password("abcdefgh"),
        status=UserStatus.active.value,
    )
    rambo.addBook(pelican)

    smith = User(
        username="test_account",
        password=UserService.encode_password("abcd1234"),
        first_name="Test",
        last_name="Account",
        status=UserStatus.disabled.value,
    )


if __name__ == "__main__":
    print("Initializing db tables and data...")
    init_data()
    print("Done.")
