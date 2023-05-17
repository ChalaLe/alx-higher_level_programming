-- This script lists the number of records with the same score
-- in the "second_table" table of the "hbtn_0c_0" database in MySQL Server

-- Retrieve the score and count of records from the "second_table" table
-- Group the results by the score
-- Order the results by score in descending order
SELECT score, COUNT(score) AS number
FROM hbtn_0c_0.second_table
GROUP BY score
ORDER BY score DESC;
