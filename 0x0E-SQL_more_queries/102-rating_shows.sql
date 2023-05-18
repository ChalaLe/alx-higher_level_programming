-- This script lists all shows from the hbtn_0d_tvshows_rate table by their rating
-- Records are ordered by descending rating

-- Select the title and sum of rates from the tv_shows and tv_show_ratings tables
-- Perform an inner join between the tv_shows and tv_show_ratings tables
-- The ON clause specifies the relationship between the tables based on their respective ids
-- Group the results by title
-- Calculate the sum of rates for each title using the SUM function
-- Order the results by descending rating

SELECT `title`, SUM(`rate`) AS `rating`
FROM `tv_shows` AS t
INNER JOIN `tv_show_ratings` AS r
ON t.`id` = r.`show_id`
GROUP BY `title`
ORDER BY `rating` DESC;
