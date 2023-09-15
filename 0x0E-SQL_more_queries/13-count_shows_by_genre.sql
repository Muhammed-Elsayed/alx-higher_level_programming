-- all genres from hbtn_0d_tvshows
 SELECT tv_genres.name AS genres, COUNT(tv_show_genres.genre_id) AS num FROM tv_genres INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id GROUP BY genres ORDER BY num DESC;
