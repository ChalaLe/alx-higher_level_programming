-- This script lists all shows and genres linked to the shows in the database hbtn_0d_tvshows
-- Records are ordered by ascending show title and genre name

-- Select the show title and genre name from the tv_shows and tv_genres tables
-- Perform LEFT JOINs between the tv_shows, tv_show_genres, and tv_genres tables
-- to retrieve all shows and their linked genres
-- The ON clauses specify the relationships between the tables based on their respective ids and genre_id
-- The ORDER BY clause orders the results by ascending show title and genre name

SELECT t.`title`, g.`name`
FROM `tv_shows` AS t
LEFT JOIN `tv_show_genres` AS s ON t.`id` = s.`show_id`
LEFT JOIN `tv_genres` AS g ON s.`genre_id` = g.`id`
ORDER BY t.`title` ASC, g.`name` ASC;
