CREATE TABLE secret_user(
    user_id SERIAL PRIMARY KEY,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    code_name VARCHAR(100),
    country VARCHAR(50),
    organization VARCHAR(100),
    salary INT,
    knows_kung_fu BOOLEAN
)