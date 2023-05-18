-- This script lists all shows contained in the database hbtn_0d_tvshows
-- Displays NULL for shows without genres

-- Select the show title and genre_id
-- by performing a LEFT JOIN between the tv_shows table and the tv_show_genres table
-- on the matching id and show_id columns respectively
-- The results are ordered by ascending tv_shows.title and tv_show_genres.genre_id
SELECT s.`title`, g.`genre_id`
FROM `tv_shows` AS s
LEFT JOIN `tv_show_genres` AS g ON s.`id` = g.`show_id`
ORDER BY s.`title`, g.`genre_id`;
