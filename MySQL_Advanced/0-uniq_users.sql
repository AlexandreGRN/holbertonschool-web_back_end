-- Create users taable if it does not exist
CREATE TABLE IF NOT EXISTS users (
    -- id int auto increment primary key
    id INT AUTO_INCREMENT PRIMARY KEY,
    -- email string not null unique
    email VARCHAR(255) NOT NULL UNIQUE,
    -- name string nullable
    name VARCHAR(255)
);
