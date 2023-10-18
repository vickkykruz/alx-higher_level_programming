-- This is a SQL Script that lists all Comedy shows in the database
-- hbtn_0d_tvshows.
SELECT shows.title FROM tv_shows AS shows
INNER JOIN tv_show_genres AS s_genres ON shows.id = s_genres.show_id
INNER JOIN tv_genres AS genres ON s_genres.genre_id = genres.id
WHERE genres.name = 'Comedy'
ORDER BY shows.title
