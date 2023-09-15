-- database dump of hbtn_0d_tvshows to your MySQL
 SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows LEFT JOIN tv_show_genres ON show_id = tv_shows.id ORDER BY title, tv_show_genres.genre_id ASC;
