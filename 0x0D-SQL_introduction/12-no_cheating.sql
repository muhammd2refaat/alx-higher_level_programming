-- 12. Cheating is bad
-- this script lists all records with a score of a Bob to 10 in the table second_table

SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC
