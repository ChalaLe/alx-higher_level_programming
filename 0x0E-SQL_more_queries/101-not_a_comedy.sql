-- This script lists all shows without the comedy genre in the hbtn_0d_tvshows database
-- Records are ordered by ascending show title

-- Select the distinct show titles from the tv_shows table
-- Perform LEFT JOINs between the tv_shows, tv_show_genres, and tv_genres tables
-- to retrieve the genres linked to shows
-- The ON clauses specify the relationships between the tables based on their respective ids and genre_id
-- The WHERE clause filters out the shows that have the comedy genre
-- The NOT IN clause specifies the subquery that retrieves the shows with the comedy genre
-- The ORDER BY clause orders the results by ascending show title

SELECT DISTINCT t.`title`
FROM `tv_shows` AS t
LEFT JOIN `tv_show_genres` AS s ON s.`show_id` = t.`id`
LEFT JOIN `tv_genres` AS g ON g.`id` = s.`genre_id`
WHERE t.`title` NOT IN (
    SELECT t.`title`
    FROM `tv_shows` AS t
    INNER JOIN `tv_show_genres` AS s ON s.`show_id` = t.`id`
    INNER JOIN `tv_genres` AS g ON g.`id` = s.`genre_id`
    WHERE g.`name` = "Comedy"
)
ORDER BY t.`title` ASC;
