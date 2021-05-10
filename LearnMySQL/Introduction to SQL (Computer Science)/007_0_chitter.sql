DROP TABLE chitter_user, post, follower;
CREATE TABLE chitter_user(
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(100),
    encrypted_password VARCHAR(100),
    email VARCHAR(100),
    date_joined DATE
);

CREATE TABLE post(
    post_id SERIAL PRIMARY KEY,
    user_id INT NOT NULL,
    post_text VARCHAR(100),
    posted_on TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES chitter_user(user_id) ON DELETE CASCADE
   );

CREATE TABLE follower( 
    follower_id INT NOT NULL,
    user_id INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES chitter_user(user_id) ON DELETE CASCADE
);

INSERT INTO chitter_user(user_id,username,encrypted_password,email,date_joined)
VALUES  (DEFAULT,'firstuser','d63dc919e2dc30d2','fakeemail@fakedomain.fake','2019-02-25'),
        (DEFAULT,'seconduser','d63dc919e2dc30d3','fakeemail2@fakedomain.fake','2019-02-26');

INSERT INTO post
    (user_id,post_text)
VALUES
    (1,'Hello World!'),
    (2,'Hello Solar System!');

SELECT * FROM chitter_user;
SELECT * FROM post;
