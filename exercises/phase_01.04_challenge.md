# User Story
```
As a person who loves movies,
So I can list all my favourite movies
I want to see a list of movies' titles.

As a person who loves movies,
So I can list all my favourite movies
I want to see a list of movies' genres.

As a person who loves movies,
So I can list all my favourite movies
I want to see a list of movies' release years.
```

# 1. Extract nouns from user story/spec
```
Nouns:
movies, titles, genres, release year
```

# 2. Infer the table name and columns
| Record             | Properties        |
| -------------------|------------------ |
| movies           | title, genre, release year      |

# 3. Decide the column types
```
id: SERIAL
title: text
genre: text
release_year: int
```

# 4. Write the SQL
```
-- file student_directory_1

CREATE TABLE students (
    id SERIAL PRIMARY KEY
    name text
    genre text
    release_year int
)
```
