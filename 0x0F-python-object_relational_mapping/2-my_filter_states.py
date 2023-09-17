#!/usr/bin/python3

"""
List all the states in the db
"""
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)

    cur = db.cursor()

    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC"\
            .format(sys.argv[4])
    cur.execute(query)

    results = cur.fetchall()

    for row in results:
        print(row)

    cur.close()
    db.close()
