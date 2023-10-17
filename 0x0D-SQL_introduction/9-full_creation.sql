-- Write a script that creates a table second_table in the database hbtn_0c_0 in
-- your MySQL server and add multiples rows.
CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
);
-- Insert the first row to the table
INSERT INTO second_table
VALUES(1, "John", 10);
-- Insert the secound row to the table
INSERT INTO second_table
VALUES(2, "Alex", 3);
-- Insert the third row to the table
INSERT INTO second_table
VALUES(3, "Bob", 14);
-- Insert the fourth row to the table
INSERT INTO second_table
VALUES(4, "George", 8);