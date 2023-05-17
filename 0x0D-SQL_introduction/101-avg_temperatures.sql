-- This script displays the average temperature by city
-- in the "temperatures" table, ordered by temperature in descending order

-- Retrieve the city and average temperature from the "temperatures" table
-- Group the results by city
-- Calculate the average temperature using AVG(value)
-- Order the results by average temperature in descending order
SELECT city, AVG(value) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
