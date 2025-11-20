-- Exported definition from 2025-11-20T11:31:15
-- Class models.Author
-- Database: sqlite
CREATE TABLE author (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    date_of_birth DATE NOT NULL
)
