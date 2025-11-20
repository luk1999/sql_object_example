-- Exported definition from 2025-11-20T11:31:15
-- Class models.Book
-- Database: sqlite
CREATE TABLE book (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    author_id INT NOT NULL CONSTRAINT author_id_exists REFERENCES author(id) ,
    title VARCHAR(100) NOT NULL,
    year INT NOT NULL,
    genre VARCHAR(13) CHECK (genre in ('adventure', 'autobiography', 'biography', 'fantasy', 'history', 'horror', 'mystery', 'poetry', 'romance', 'sci_fi', 'thriller')) NOT NULL
);
CREATE TABLE book_user (
book_id INT NOT NULL,
user_id INT NOT NULL
)
