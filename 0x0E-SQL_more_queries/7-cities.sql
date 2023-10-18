-- This is a SQL Script that creates the database hbtn_0d_usa and the table
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
-- Create a TABLE
CREATE TABLE IF NOT EXISTS `hbtn_0d_usa`.`cities` (
	PRIMARY KEY (`id`),
	`id` INT NOT NULL AUTO_INCREMENT,
	`state_id` INT NOT NULL,
	`name` VARCHAR(256) NOT NULL,
	FOREIGN KEY (`state_id`)
	REFERENCES `hbtn_0d_usa`.`states`(`id`)
);
