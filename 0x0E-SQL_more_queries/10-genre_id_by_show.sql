-- 10. Genre ID by show
-- lists all genres in the database hbtn_0d_tvshows

SELECT shows.title, genres.id
FROM tv_shows AS shows
INNER JOIN tv_show_genres AS show_genres
ON shows.id = show_genres.show_id
ORDER BY shows.title, genres.id
