#!/usr/bin/python3
"""
Write a script that lists all states from the database hbtn_0e_0_usa:
    => Your script should take 3 arguments: mysql username, mysql password
        and database name
    => mysql password and database name (no argument validation needed)
    => Your script should connect to a MySQL server running on localhost
        at port 3306
    => Results must be sorted in ascending order by states.id
"""


import MySQLdb
import sys

if __name__ == "__main__":
    # To handle the connection that takes 3 arguments
    db = MySQLdb.connect(
            host='localhost',
            user='{}'.format(sys.argv[1]),
            password='{}'.format(sys.argv[2]),
            database='{}'.format(sys.argv[3]),
            port=3306)
    cur = db.cursor()

    cur.execute(
            """SELECT * FROM states ORDER BY states.id ASC""")

    # To fetch the data
    row = cur.fetchall()

    for data in row:
        print(data)
