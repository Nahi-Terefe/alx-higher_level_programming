#!/usr/bin/python3
""" Lists all the state filter by state name start with N"""

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

    cursor.execute("SELECT * FROM states where \
        states.name like 'N%' ORDER BY states.id ASC")
    fetch = cursor.fetchall()
    for row in fetch:
        print(row)
