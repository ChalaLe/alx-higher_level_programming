-- This script displays the maximum temperature of each state
-- in the "temperatures" table, ordered by state name

-- Retrieve the state and maximum temperature from the "temperatures" table
-- Group the results by state
-- Calculate the maximum temperature using MAX(value)
-- Order the results by state name
SELECT state, MAX(value) AS max_temp
FROM temperatures
GROUP BY state
ORDER BY state;
