-- This script lists all rows of the "second_table" table from the "hbtn_0c_0" database
-- The results display the score and name columns, ordered by score in descending order
-- Only rows with a score greater than or equal to 10 are included

-- Retrieve all rows from the "second_table" table
-- Display the score and name columns
-- Include only rows with a score greater than or equal to 10
-- Order the results by score in descending order
SELECT score, name FROM hbtn_0c_0.second_table WHERE score >= 10 ORDER BY score DESC;
