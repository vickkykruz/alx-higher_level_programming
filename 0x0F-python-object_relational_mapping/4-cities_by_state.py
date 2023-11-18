#!/usr/bin/python3

"""
Write a script that lists all cities from the database hbtn_0e_4_usa
    => Your script should take 3 arguments: mysql username, mysql password and
        database name
    => You must use the module MySQLdb (import MySQLdb)
    => Your script should connect to a MySQL server running on localhost at
        port 3306
"""


import MySQLdb
import sys


if __name__ == "__main__":
    # Connection
    db = MySQLdb.connect(
            host='localhost',
            user='{}'.format(sys.argv[1]),
            password='{}'.format(sys.argv[2]),
            database='{}'.format(sys.argv[3]),
            port=3306)

    cur = db.cursor()

    cur.execute(
            """SELECT cities.id, cities.name, states.name
            FROM cities INNER JOIN states
            ON cities.state_id = states.id
            ORDER BY cities.id ASC;""")

    rows = cur.fetchall()

    for row in rows:
        print(row)
