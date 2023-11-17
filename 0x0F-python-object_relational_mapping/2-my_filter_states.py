#!/usr/bin/python3

"""
Write a script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument
    => Your script should take 4 arguments: mysql username, mysql password,
        database name and state name searched
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

    cur.execute("""SELECT * FROM states WHERE CONVERT (`name` USING Latin1)
                COLLATE Latin1_General_CS = '{}';""".format(sys.argv[4]))

    row = cur.fetchall()
    for data in row:
        print(data)
