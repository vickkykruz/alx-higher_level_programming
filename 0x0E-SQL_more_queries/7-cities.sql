-- This is a SQL Script that creates the database hbtn_0d_usa and the table
-- cities (in the database hbtn_0d_usa) on your MySQL server.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Use the DATABASE
USE hbtn_0d_usa;
-- Create a TABLE
CREATE TABLE IF NOT EXISTS cities (
	id INT NOT NULL AUTO_INCREMEMT,
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY (state_id) REFERENCES states(id)
);
