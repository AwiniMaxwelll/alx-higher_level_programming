#!/usr/bin/python3
""" select all states with a name starting with N from the hbtn_0e_0_usa """
import MYSQLdb
import sys


if __name__ == "__main__":
    db = mysqldb.connect(host="localhost", user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)
    c = db.cursor()
    c.execute("""SELECTE * FROM states 
                WHERE name LIKE BINARY 'N%' ORDER states.id""")
    rows = c.fetchall()
    for row in rows:
        print(row)
    c.close()
    db.close()
