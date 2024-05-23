-- 14. My genres
-- lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each

SELECT name
FROM tv_genres LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
LEFT JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id WHERE tv_shows.title = "Dexter"
GROUP BY name ORDER BY name ASC;