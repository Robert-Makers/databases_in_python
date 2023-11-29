# User Story
```
As a coach
So I can get to know all students
I want to see a list of students' names.

As a coach
So I can get to know all students
I want to see a list of students' cohorts.
```

# 1. Extract nouns from user story/spec
```
Nouns:
Students, names, cohorts
```

# 2. Infer the table name and columns
| Record             | Properties        |
| -------------------|------------------ |
| students           | name, cohort      |

# 3. Decide the column types
```
id: SERIAL
name: text
cohort: text
```

# 4. Write the SQL
```
-- file student_directory_1

CREATE TABLE students {
    id SERIAL PRIMARY KEY
    name text
    cohort text
}
```
