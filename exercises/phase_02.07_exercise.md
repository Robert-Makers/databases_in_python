# User Story
```
As a social network user,
So I can have my information registered,
I'd like to have a user account with my email address.

As a social network user,
So I can have my information registered,
I'd like to have a user account with my username.

As a social network user,
So I can write on my timeline,
I'd like to create posts associated with my user account.

As a social network user,
So I can write on my timeline,
I'd like each of my posts to have a title and a content.

As a social network user,
So I can know who reads my posts,
I'd like each of my posts to have a number of views.
```

# 1. Extract nouns from the user stories or specification
```
Nouns:
User account, email address, username, posts, title, content, view
```

# 2. Infer the Table Name and Columns
| Record             | Properties         |
| -------------------|------------------- |
| users              | username, email    |
| posts              | title, content, views |

# 3. Decide the column types
```
Table: Users
id SERIAL
username text
email text

Table: Posts
id SERIAL
title text
content text
views int
```

# 4. Decide on The Tables Relationship
posts belong to a user
posts will have a foreign id

# 5. Write the SQL
```
-- file: social_network.sql

DROP TABLE IF EXISTS users;
DROP SEQUENCE IF EXISTS users_id_seq;
DROP TABLE IF EXISTS posts;
DROP SEQUENCE IF EXISTS posts_id_seq;


CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username text,
    email text
);

CREATE SEQUENCE IF NOT EXISTS posts_id_seq;
CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    title text,
    content text,
    user_id int,
    constraint fk_user foreign key(user_id) references users(id) on delete cascade
);
```