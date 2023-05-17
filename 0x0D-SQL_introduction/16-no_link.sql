-- This script lists all records in a table except those with no value in the name column

-- Retrieve the score and name columns from the "second_table" table
-- Include only rows where the name is not NULL
-- Order the results by score in descending order
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
