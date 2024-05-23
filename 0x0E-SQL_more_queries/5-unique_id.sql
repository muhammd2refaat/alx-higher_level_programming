-- 5. Unique ID
-- this script creates the table unique_id
--  unique_id INT with the default value 1 and name VARCHAR(256)

CREATE TABLE IF NOT EXISTS unique_id (id INT DEFAULT 1 UNIQUE, name VARCHAR(256));
