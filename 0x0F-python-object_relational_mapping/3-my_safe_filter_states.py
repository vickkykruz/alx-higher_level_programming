#!/usr/bin/python3

"""
write a script that takes in arguments and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument. But this time, write
one that is safe from MySQL injections!
    => Your script should take 4 arguments: mysql username, mysql password,
        database name and state name searched
    => You must use the module MySQLdb (import MySQLdb)
"""


import MySQLdb
import sys


if __name__ == "__main__":
    # CONNECTION
    db = MySQLdb.connect(
            host='localhost',
            user='{}'.format(sys.argv[1]),
            password='{}'.format(sys.argv[2]),
            database='{}'.format(sys.argv[3]),
            port=3306)

    cur = db.cursor()

    cur.execute(
            """SELECT * FROM states WHERE CONVERT(`name` USING Latin1)
            COLLATE Latin1_General_CS = '{}';""".format(sys.argv[4]))

    row = cur.fetchall()

    for data in row:
        print(data)
