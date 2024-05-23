-- 12. No genre
-- lists all shows without the genre Comedy in the database hbtn_0d_tvshows

SELECT shows.title
FROM tv_shows AS shows
LEFT JOIN tv_show_genres AS genres
ON tv_shows.id = genres.show_id
WHERE genres.genre_id IS NULL
ORDER BY shows.title, genres.genre_id
