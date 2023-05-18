-- This script lists all cities in the database hbtn_0d_usa along with their state names

-- Select the city id, city name, and state name
-- by joining the cities table with the states table
-- on the matching state_id and id columns respectively
-- The results are ordered by ascending cities.id
SELECT c.`id`, c.`name`, s.`name`
FROM `cities` AS c
INNER JOIN `states` AS s ON c.`state_id` = s.`id`
ORDER BY c.`id`;
