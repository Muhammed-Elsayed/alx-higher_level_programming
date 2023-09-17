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

    cur.execute("""SELECT cities.id, cities.name, states.name
    FROM cities
    LEFT JOIN states ON cities.state_id = states.id
    ORDER BY cities.id ASC""")
    results = cur.fetchall()
    count = 0
    for row in results:
        if (row[2] == sys.argv[4]):
            if count > 0:
                print(", ", end="")
            print(row[1], end="")
            count += 1
    print()
    cur.close()
    db.close()
