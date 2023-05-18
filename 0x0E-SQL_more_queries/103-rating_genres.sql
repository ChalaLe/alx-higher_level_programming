-- This script lists all genres in the hbtn_0d_tvshows_rate database by their rating
-- Records are ordered by descending rating

-- Select the name and sum of rates from the tv_genres, tv_show_genres, and tv_show_ratings tables
-- Perform inner joins between the tables based on their respective ids
-- The ON clauses specify the relationships between the tables
-- Group the results by name
-- Calculate the sum of rates for each genre using the SUM function
-- Order the results by descending rating

SELECT `name`, SUM(`rate`) AS `rating`
FROM `tv_genres` AS g
INNER JOIN `tv_show_genres` AS s
ON s.`genre_id` = g.`id`
INNER JOIN `tv_show_ratings` AS r
ON r.`show_id` = s.`show_id`
GROUP BY `name`
ORDER BY `rating` DESC;
