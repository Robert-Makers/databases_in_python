
DROP TABLE IF EXISTS users;
DROP SEQUENCE IF EXISTS users_id_seq;


CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username text,
    email text
);

INSERT INTO users (username, email) VALUES ('mikeyP', 'mike_p@gmail.com');
INSERT INTO users (username, email) VALUES ('melC', 'melmel@gmail.com');
INSERT INTO users (username, email) VALUES ('melB', 'sporty@gmail.com');
INSERT INTO users (username, email) VALUES ('viccy', 'posh_v@gmail.com');

DROP TABLE IF EXISTS posts;
DROP SEQUENCE IF EXISTS posts_id_seq;

CREATE SEQUENCE IF NOT EXISTS posts_id_seq;
CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    title text,
    content text,
    views int,
    user_id int
);