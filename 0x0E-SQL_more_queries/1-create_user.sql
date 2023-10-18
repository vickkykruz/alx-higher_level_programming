-- This is a sql script that create a user
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost'
IDENTIFIED BY 'user_0d_1_pwd';
-- Grand all the permission
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
