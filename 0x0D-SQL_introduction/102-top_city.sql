-- This script displays the average temperature of the top 3 cities
-- during July and August in the "temperatures" table, ordered by temperature in descending order

-- Retrieve the city and average temperature from the "temperatures" table
-- Filter the results to include only records with month 7 (July) or 8 (August)
-- Group the results by city
-- Calculate the average temperature using AVG(value)
-- Order the results by average temperature in descending order
-- Limit the results to the top 3 cities
SELECT city, AVG(value) AS avg_temp
FROM temperatures
WHERE month = 7 OR month = 8
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
