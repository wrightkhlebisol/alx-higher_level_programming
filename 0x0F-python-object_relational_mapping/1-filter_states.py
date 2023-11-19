#!/usr/bin/python3
""" List all states """


import MySQLdb
import sys

if __name__ == '__main__':
    host = 'localhost'
    port = '3306'
    url = f'{host}:{port}'
    args = sys.argv
    if len(args) >= 4:
        db = MySQLdb.connect(host, args[1], args[2], args[3])
        cur = db.cursor()
        query = 'SELECT * FROM states WHERE name \
        LIKE "N%" ORDER BY `id` ASC'
        res = cur.execute(query)
        rows = cur.fetchall()
        for row in rows:
            print(row)
        cur.close()
        db.close()
