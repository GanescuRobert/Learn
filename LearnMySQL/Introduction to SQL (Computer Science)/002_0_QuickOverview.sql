CREATE DATABASE social_network;
USE social_network;
CREATE TABLE users(
    user_id int,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    email VARCHAR(100)
);
ALTER TABLE users ADD encrypted_password VARCHAR(1000);

ALTER TABLE users DROP COLUMN email;

DROP TABLE users;
DROP DATABASE social_network; 