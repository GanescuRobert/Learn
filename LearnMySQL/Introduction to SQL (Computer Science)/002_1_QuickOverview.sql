#CREATE DATABASE social_network;

USE social_network;
/*CREATE TABLE users(
    user_id int,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    email VARCHAR(255),
    encrypted_password VARCHAR(1000)
);
CREATE TABLE movies(
    movie_id int,
    title VARCHAR(100),
    description VARCHAR(100),
    price VARCHAR(255)
);

CREATE TABLE purchases(
    user_id int,
    movie_id int,
    purchase_date VARCHAR(255),
    purchase_price VARCHAR(100)
);

INSERT INTO movies(movie_id,title,description,price) VALUES(1,'Gattaca','Movie or documentary?',4.99);

INSERT INTO movies(title,price) VALUES('Star Wars',8.99);
INSERT INTO movies(title,price) VALUES('Logan\'s Run',3.99);
INSERT INTO movies(title,price) VALUES('Solaris',2.99);
INSERT INTO movies(title,price) VALUES('Jaws',5.25);
INSERT INTO movies(title,price) VALUES('Silent Running',3.00);
*/

UPDATE movies SET price=0.99 WHERE title REGEXP '.*? .*?';
DELETE FROM movies WHERE NOT title REGEXP '.{8}?';

SELECT title,price FROM movies ORDER BY price DESC;

DROP DATABASE social_network;