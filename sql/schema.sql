CREATE DATABASE IF NOT EXISTS censo_escolar;

USE censo_escolar;

CREATE TABLE usuario (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(100) NOT NULL
);
