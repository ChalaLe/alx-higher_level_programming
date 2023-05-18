-- This script lists all genres of the show "Dexter" in the database hbtn_0d_tvshows
-- Records are ordered by ascending genre name

-- Select the genre name from the tv_genres table
-- Perform INNER JOINs between the tv_genres, tv_show_genres, and tv_shows tables
-- to retrieve the genres linked to the show "Dexter"
-- The ON clauses specify the relationships between the tables based on their respective ids and show_id
-- Apply a WHERE condition to filter the results to only include the show "Dexter" using the t.`title` column
-- The ORDER BY clause orders the results by ascending genre name

SELECT g.`name`
FROM `tv_genres` AS g
INNER JOIN `tv_show_genres` AS s ON g.`id` = s.`genre_id`
INNER JOIN `tv_shows` AS t ON t.`id` = s.`show_id`
WHERE t.`title` = "Dexter"
ORDER BY g.`name`;
