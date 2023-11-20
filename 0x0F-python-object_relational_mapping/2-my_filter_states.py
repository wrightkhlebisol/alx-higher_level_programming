#!/usr/bin/python3
""" Filter states by user input """


import MySQLdb
import sys

if __name__ == '__main__':
    host = 'localhost'
    port = 3306
    args = sys.argv
    if len(args) >= 4:
        db = MySQLdb.connect(
            port=port,
            host=host,
            user=args[1],
            password=args[2],
            database=args[3]
        )
        """ Create a cursor """
        cur = db.cursor()
        query = "SELECT * FROM states WHERE name = '{}' \
            ORDER BY id ASC".format(args[4])
        cur.execute(query)
        rows = cur.fetchall()
        for row in rows:
            print(row)
        cur.close()
        db.close()
