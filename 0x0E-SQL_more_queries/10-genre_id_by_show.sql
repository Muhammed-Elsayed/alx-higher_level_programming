-- lists all shows contained in hbtn_0d_tvshows
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows INNER JOIN tv_show_genres ON show_id = tv_shows.id ORDER BYtitle ASC;
