-- 2. Read user
-- this script creates the MySQL user user_0d_2 and the user user_0d_2
-- Create the database if it does not exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Create the user if it does not exist
-- Set the password of the user to user_0d_2_pwd
CREATE USER IF NOT EXISTS user_0d_2@localhost IDENTIFIED BY 'user_0d_2_pwd';

-- Grant SELECT privilege on hbtn_0d_2.* to user_0d_2@localhost
GRANT SELECT ON hbtn_0d_2.* TO user_0d_2@localhost;

-- Flush the privileges so that the changes take effect immediately
FLUSH PRIVILEGES;
