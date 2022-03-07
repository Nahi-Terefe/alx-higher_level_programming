#!/usr/bin/python3
""" Lists all the state filter by state name start with N"""


if __name__ == "__main__":

    import MySQLdb
    import sys

    db_user = sys.argv[1]
    db_pass = sys.argv[2]
    db_name = sys.argv[3]

    database = MySQLdb.connect(host='localhost',
                               port=3306,
                               user=db_user,
                               password=db_pass,
                               db=db_name,
                               charset="utf8")

    cursor = database.cursor()

    cursor.execute("""SELECT * FROM states WHERE name
                LIKE BINARY 'N%' ORDER BY states.id ASC""")
    fetch = cursor.fetchall()
    for row in fetch:
        print(row)

    cursor.close()
    database.close()
