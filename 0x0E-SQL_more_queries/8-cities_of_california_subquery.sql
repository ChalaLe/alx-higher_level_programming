-- This script lists all cities of CA in the database hbtn_0d_usa

-- Select the id and name columns from the cities table
-- where the state_id is in the subquery result
-- which selects the id from the states table where the name is "California"
-- The results are ordered by ascending cities.id
SELECT `id`, `name`
FROM `cities`
WHERE `state_id` IN (
    SELECT `id`
    FROM `states`
    WHERE `name` = "California"
)
ORDER BY `id`;
