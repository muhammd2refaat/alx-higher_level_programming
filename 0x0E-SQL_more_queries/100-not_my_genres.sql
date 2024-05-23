-- 17. Not my genre
-- Lists all shows contained in hbtn_0d_tvshows
-- that have no genre linked
-- Records are ordered by ascending tv_shows.title

SELECT tv_shows.title, tv_genres.name
FROM tv_shows
LEFT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres
ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_genres.name IS NULL
ORDER BY tv_shows.title, tv_genres.name
