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
    WHERE states.name = 'Texas'
    ORDER BY cities.id ASC""")
    results = cur.fetchall()
    count = 0
    for row in results:
        print(row[1], end="")
        count += 1
        if (count != len(results)):
            print("", end=", ")
    print("")
    cur.close()
    db.close()
