-- This script updates the score of 'Bob' to 10 in the "second_table" table
-- It uses the name field as the condition for the update

-- Update the score in the "second_table" table
-- Set the score to 10
-- Only update the row where the name is 'Bob'
UPDATE second_table SET score = 10 WHERE name = 'Bob';
