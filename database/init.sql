DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    role TEXT NOT NULL
);

INSERT INTO users (username, password, role)
VALUES
('admin','ADMIN','admin'),
('john','john123','employee'),
('alice','alice123','employee');