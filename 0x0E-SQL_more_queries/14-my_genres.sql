-- This is a SQL script file that uses the hbtn_0d_tvshows database to lists
-- all genres of the show Dexter.
SELECT genres.name FROM tv_genres AS genres 
INNER JOIN tv_show_genres AS s_genres ON genres.id = s_genres.genre_id 
INNER JOIN tv_shows AS shows ON s_genres.show_id = shows.id 
WHERE shows.title = 'Dexter' 
ORDER BY genres.name
