-- create user table if not exists
CREATE TABLE IF NOT EXISTS users (
    -- id int auto increment primary key
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    -- email string not null unique
    email VARCHAR(255) NOT NULL UNIQUE,
    -- name string nullable
    name VARCHAR(255),
    -- country enum not null default US
    country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US'
);
