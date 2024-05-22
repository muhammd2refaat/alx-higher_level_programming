-- 15. Number by score
-- List the number of records with the same score in the table second_table of the database hbtn_0c_0 in your MySQL server
-- The result should display:
-- score number
-- 5 records

SELECT score, COUNT(score) AS number FROM second_table GROUP BY score ORDER BY score DESC
