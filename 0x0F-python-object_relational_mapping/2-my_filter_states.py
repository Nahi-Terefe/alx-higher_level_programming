#!/usr/bin/python3
""" a script that takes in an argument and displays all
    values in the states table of hbtn_0e_0_usa where
    name matches the argument"""


if __name__ == "__main__":

    import MySQLdb
    import sys

    db_user = sys.argv[1]
    db_pass = sys.argv[2]
    db_name = sys.argv[3]
    given_state = sys.argv[4]

    database = MySQLdb.connect(host='localhost',
                               port=3306,
                               user=db_user,
                               password=db_pass,
                               db=db_name)

    cursor = database.cursor()

    cursor.execute("SELECT * FROM states\
        WHERE  states.name = %s\
        ORDER BY states.id ASC;", (given_state,))

    fetch = cursor.fetchall()
    for row in fetch:
        print(row)

    cursor.close()
    database.close()
