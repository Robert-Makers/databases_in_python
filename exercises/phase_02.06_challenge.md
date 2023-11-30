# User Story
```
As a blogger
So I can write interesting stuff
I want to write posts having a title.

As a blogger
So I can write interesting stuff
I want to write posts having a content.

As a blogger
So I can let people comment on interesting stuff
I want to allow comments on my posts.

As a blogger
So I can let people comment on interesting stuff
I want the comments to have a content.

As a blogger
So I can let people comment on interesting stuff
I want the author to include their name in comments.
```

# 1. Extract nouns from the user stories or specification
```
Nouns:
Posts, title, content, comments, comment_content, comment_author
```

# 2. Infer the Table Name and Columns
| Record             | Properties         |
| -------------------|------------------- |
| posts              | title, content     |
| comments           | content, author    |

# 3. Decide the column types
```
Table: Posts
id SERIAL
title text
content text

Table: Comments
id SERIAL
content text
author text
post id
```

# 4. Decide on The Tables Relationship
comments belong to a post
comments will have a foreign id

# 5. Write the SQL
```
-- file: blog_directory.sql

CREATE TABLE posts (
  id SERIAL PRIMARY KEY,
  title text,
  content text
);

CREATE TABLE students (
  id SERIAL PRIMARY KEY,
  content text,
  author text,
  post_id int,
  constraint fk_post foreign key(post_id) references posts(id) on delete cascade
);
```