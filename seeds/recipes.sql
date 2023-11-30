DROP TABLE IF EXISTS recipes;
DROP SEQUENCE IF EXISTS recipes_id_seq;

CREATE SEQUENCE IF NOT EXISTS recipes_id_seq;
CREATE TABLE recipes (
    id SERIAL PRIMARY KEY,
    name text,
    cooking_time int,
    rating int
);

INSERT INTO recipes (name, cooking_time, rating) VALUES ('Lasagna', 60, 4);
INSERT INTO recipes (name, cooking_time, rating) VALUES ('Pizza', 20, 5);
INSERT INTO recipes (name, cooking_time, rating) VALUES ('Mushroom Soup', 10, 2);
INSERT INTO recipes (name, cooking_time, rating) VALUES ('Fajitas', 30, 4);