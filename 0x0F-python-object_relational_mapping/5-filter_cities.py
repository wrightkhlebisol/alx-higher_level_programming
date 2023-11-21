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
        query = "SELECT name FROM cities \
                WHERE state_id = (SELECT id FROM states WHERE name = %s) \
                ORDER BY id ASC"
        res = cur.execute(query, (args[4],))
        rows = cur.fetchall()
        for i, row in enumerate(rows):
            if i == res - 1:
                print(row[0])
            else:
                print(row[0], end=', ')

        cur.close()
        db.close()
