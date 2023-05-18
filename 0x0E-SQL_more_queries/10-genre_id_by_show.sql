-- This script lists all shows in hbtn_0d_tvshows that have at least one genre linked

-- Select the show title and genre_id
-- by joining the tv_shows table with the tv_show_genres table
-- on the matching id and show_id columns respectively
-- The results are ordered by ascending tv_shows.title and tv_show_genres.genre_id
SELECT s.`title`, g.`genre_id`
FROM `tv_shows` AS s
INNER JOIN `tv_show_genres` AS g ON s.`id` = g.`show_id`
ORDER BY s.`title`, g.`genre_id`;
