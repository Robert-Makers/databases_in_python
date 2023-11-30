# User Story
```
As a coach
So I can get to know all students
I want to see a list of students' names.

As a coach
So I can get to know all students
I want to see a list of cohorts' names.

As a coach
So I can get to know all students
I want to see a list of cohorts' starting dates.

As a coach
So I can get to know all students
I want to see a list of students' cohorts.
```

# 1. Extract nouns from the user stories or specification
```
Nouns:
Students, cohort names, cohort start dates, students cohorts
```

# 2. Infer the Table Name and Columns
| Record             | Properties         |
| -------------------|------------------- |
| cohorts            | name, starting date|
| students           | name, cohort       |

# 3. Decide the column types
```
Table: Cohorts
id SERIAL
name text
starting date date

Table: Students
id SERIAL
name text
cohort int
```

# 4. Decide on The Tables Relationship
students belong to a cohort
students will have a foreign id

# 5. Write the SQL
```
-- file: student_directory_2.sql

CREATE TABLE cohorts (
  id SERIAL PRIMARY KEY,
  name text,
  starting_date date
);

CREATE TABLE students (
  id SERIAL PRIMARY KEY,
  name text,
  cohort_id int,
  constraint fk_cohort foreign key(cohort_id) references cohorts(id) on delete cascade
);

```