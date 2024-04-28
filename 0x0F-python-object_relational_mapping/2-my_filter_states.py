#!/usr/bin/python3
"""  display all table in a state where name matched the arg """
import MYSQLdb
import sys


if __name__ == "__main__":
    db = MYSQLdb.connect(host="localhost", user=sys.argv[1], passwd=sys.argv[2],
                        db=sys.argv[3], port=3306)
   c  = db.cursor()
   c.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'".format(sys.argv[4]))
   rows = c.fetchall()
   for row in rows:
       print()
    c.close()
    db.close()
