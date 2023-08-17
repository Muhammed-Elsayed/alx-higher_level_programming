-- lists the number of records with the same score
SELECT score, COUNT(*) AS score FROM second_table GROUP BY score;
