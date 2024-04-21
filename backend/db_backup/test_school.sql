create database if not exists test_school;

use test_school;


CREATE TABLE IF NOT EXISTS users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    email VARCHAR(50),
    password VARCHAR(50),
    first_name VARCHAR(50),
    last_name VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS tests (
    test_id INT PRIMARY KEY AUTO_INCREMENT,
    users_id INT NOT NULL,
    article VARCHAR(50),
    config VARCHAR(50),
    state INT,
    FOREIGN KEY (users_id) REFERENCES users (users_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS transactions_test (
    transaction_id INT PRIMARY KEY AUTO_INCREMENT,
    test_id INT NOT NULL,
    FOREIGN KEY (test_id) REFERENCES users (test_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS tests_results (
    tests_results_id INT PRIMARY KEY AUTO_INCREMENT,
    test_id INT NOT NULL,
    transaction_id INT NOT NULL,
    test_answers VARCHAR(50),
    session_id INT NOT NULL,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    FOREIGN KEY (test_id) REFERENCES tests (test_id) ON DELETE CASCADE,
    FOREIGN KEY (transaction_id) REFERENCES transactions_test (transaction_id) ON DELETE CASCADE,
)