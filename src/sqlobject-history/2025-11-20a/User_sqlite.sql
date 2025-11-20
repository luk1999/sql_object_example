-- Exported definition from 2025-11-20T11:31:51
-- Class models.User
-- Database: sqlite
CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(32),
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    status VARCHAR(8) CHECK (status in ('inactive', 'active', 'disabled')) NOT NULL
)
