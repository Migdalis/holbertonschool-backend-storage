-- Script that creates a table users
CREATE TABLE IF NOT EXISTS  users (
    PRIMARY KEY (id),
    id INT AUTO_INCREMENT,
    email VARCHAR(255) UNIQUE NOT NULL,
    name VARCHAR(255)
);
