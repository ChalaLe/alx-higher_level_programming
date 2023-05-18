-- This script lists all shows in the database hbtn_0d_tvshows without a genre linked

-- Select the show title and genre_id
-- by performing a LEFT JOIN between the tv_shows table and the tv_show_genres table
-- on the matching id and show_id columns respectively
-- The WHERE clause filters the results to show only records where genre_id is NULL
-- The results are ordered by ascending tv_shows.title and tv_show_genres.genre_id
SELECT s.`title`, g.`genre_id`
FROM `tv_shows` AS s
LEFT JOIN `tv_show_genres` AS g ON s.`id` = g.`show_id`
WHERE g.`genre_id` IS NULL
ORDER BY s.`title`, g.`genre_id`;
