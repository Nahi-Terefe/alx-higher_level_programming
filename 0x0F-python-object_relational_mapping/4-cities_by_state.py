#!/usr/bin/python3
"""
Write a script that lists all cities from the database hbtn_0e_4_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":

    db_user = sys.argv[1]
    db_pass = sys.argv[2]
    db_name = sys.argv[3]

    database = MySQLdb.connect(host='localhost',
                               port=3306,
                               user=db_user,
                               password=db_pass,
                               db=db_name)

    cursor = database.cursor()

    cursor.execute("""SELECT cities.id, cities.name, states.name
                   FROM cities JOIN states
                   ON cities.state_id = states.id
                   ORDER BY id ASC;""")

    fetch = cursor.fetchall()
    for row in fetch:
        print(row)

    cursor.close()
    database.close()
