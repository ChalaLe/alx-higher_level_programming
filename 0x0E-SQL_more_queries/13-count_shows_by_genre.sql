-- This script lists all genres from the database hbtn_0d_tvshows along with the number of shows linked to each
-- Genres without linked shows are not displayed
-- Records are ordered by descending number of shows linked

-- Select the genre name from the tv_genres table and count the number of shows linked to each genre
-- by performing an INNER JOIN between the tv_genres table and the tv_show_genres table
-- on the matching id and genre_id columns respectively
-- The results are grouped by genre name using the GROUP BY clause
-- The ORDER BY clause orders the results by descending number_of_shows
SELECT g.`name` AS `genre`,
       COUNT(*) AS `number_of_shows`
FROM `tv_genres` AS g
INNER JOIN `tv_show_genres` AS t ON g.`id` = t.`genre_id`
GROUP BY g.`name`
ORDER BY `number_of_shows` DESC;
