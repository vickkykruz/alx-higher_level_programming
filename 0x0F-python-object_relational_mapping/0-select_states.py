#!/usr/bin/python3

if __name__ == "__main__":
    import MySQLdb
    import sys

    # To handle the connection that takes 3 arguments
    db = MySQLdb.connect(
            user='{}'.format(sys.argv[1]),
            password='{}'.format(sys.argv[2]),
            database='{}'.format(sys.argv[3]),
            port=3306)
    cur = db.cursor()

    cur.execute("""SELECT * FROM states ORDER BY states.id ASC""")

    # To fetch the data
    row = cur.fetchall()

    for data in row:
        print(data)
