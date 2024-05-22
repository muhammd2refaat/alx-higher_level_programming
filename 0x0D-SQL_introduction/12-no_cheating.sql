-- 12. Cheating is bad
-- this script lists all records with a score of a Bob to 10 in the table second_table

UPDATE second_table
SET score = 10
WHERE name = "Bob"
