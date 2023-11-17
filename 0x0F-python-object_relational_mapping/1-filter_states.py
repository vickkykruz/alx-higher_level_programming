#!/usr/bin/python3
"""
Write a script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa:
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
            """ SELECT * FROM states WHERE convert(`name` USING Latin1)
            COLLATE Latin1_General_CS LIKE 'N%'; """)
    row = cur.fetchall()

    for data in row:
        print(data)
