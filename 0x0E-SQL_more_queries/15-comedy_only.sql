-- This script lists all comedy shows in the database hbtn_0d_tvshows
-- Records are ordered by descending show title

-- Select the show title from the tv_shows table
-- Perform INNER JOINs between the tv_shows, tv_show_genres, and tv_genres tables
-- to retrieve the shows that are categorized as "Comedy"
-- The ON clauses specify the relationships between the tables based on their respective ids and genre_id
-- Apply a WHERE condition to filter the results to only include shows with the genre "Comedy" using the g.`name` column
-- The ORDER BY clause orders the results by descending show title

SELECT t.`title`
FROM `tv_shows` AS t
INNER JOIN `tv_show_genres` AS s ON t.`id` = s.`show_id`
INNER JOIN `tv_genres` AS g ON g.`id` = s.`genre_id`
WHERE g.`name` = "Comedy"
ORDER BY t.`title` DESC;
