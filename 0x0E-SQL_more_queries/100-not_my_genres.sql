-- This script lists all genres from the hbtn_0d_tvshows database
-- that are not linked to the show Dexter
-- Records are sorted by ascending genre name

-- Select the distinct genre names from the tv_genres table
-- Perform INNER JOINs between the tv_genres, tv_show_genres, and tv_shows tables
-- to retrieve the genres linked to shows
-- The ON clauses specify the relationships between the tables based on their respective ids and genre_id
-- The WHERE clause filters out the genres that are linked to the show Dexter
-- The NOT IN clause specifies the subquery that retrieves the genres linked to the show Dexter
-- The ORDER BY clause orders the results by ascending genre name

SELECT DISTINCT g.`name`
FROM `tv_genres` AS g
INNER JOIN `tv_show_genres` AS s ON g.`id` = s.`genre_id`
INNER JOIN `tv_shows` AS t ON s.`show_id` = t.`id`
WHERE g.`name` NOT IN (
    SELECT g.`name`
    FROM `tv_genres` AS g
    INNER JOIN `tv_show_genres` AS s ON g.`id` = s.`genre_id`
    INNER JOIN `tv_shows` AS t ON s.`show_id` = t.`id`
    WHERE t.`title` = "Dexter"
)
ORDER BY g.`name` ASC;
