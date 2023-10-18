-- This is a SQL Script that lists all genres from hbtn_0d_tvshows and
-- displays the number of shows linked to each.
SELECT genres.name AS 'genre', COUNT(shows.show_id) AS 'number_of_shows'
FROM tv_genres AS genres INNER JOIN tv_show_genres AS shows
ON genres.id = shows.genre_id
GROUP BY genres.name
ORDER BY number_of_shows DESC;
