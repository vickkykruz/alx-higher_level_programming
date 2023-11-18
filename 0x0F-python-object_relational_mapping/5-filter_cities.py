#!/usr/bin/python3

"""
Write a script that takes in the name of a state as an argument and lists all
cities of that state, using the database hbtn_0e_4_usa
    => Your script should take 4 arguments: mysql username, mysql password,
        database name and state name
    => You must use the module MySQLdb (import MySQLdb)
    => Results must be sorted in ascending order by cities.id
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
            """SELECT cities.name FROM cities INNER JOIN states
            ON cities.state_id = states.id
            WHERE states.name = '{}';""".format(sys.argv[4]))

    rows = cur.fetchall()

    print(", ".join([row[0] for row in rows]))
