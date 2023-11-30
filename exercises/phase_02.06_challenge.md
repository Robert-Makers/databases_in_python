# User Story
```
As a food lover,
So I can stay organised and decide what to cook,
I'd like to keep a list of all my recipes with their names.

As a food lover,
So I can stay organised and decide what to cook,
I'd like to keep the average cooking time (in minutes) for each recipe.

As a food lover,
So I can stay organised and decide what to cook,
I'd like to give a rating to each of the recipes (from 1 to 5).
```

# 1. Extract nouns from user story/spec
```
Nouns:
Recipes, names, cooking time, rating
```

# 2. Infer the table name and columns
| Record             | Properties        |
| -------------------|------------------ |
| recipes           | name, cooking time, rating      |

# 3. Decide the column types
```
id: SERIAL
name: text
cooking_time: int
rating: int
```

# 4. Write the SQL
```
-- file student_directory_1

CREATE TABLE students {
    id SERIAL PRIMARY KEY
    name text,
    cooking_time int,
    rating int
}
```
