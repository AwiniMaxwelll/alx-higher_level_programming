#!/usr/bin/python3

"""write a script that list all the states from the database in hbtn_0e_0_usa"""
import sys
import mysqldb


db = mysqldb.connect(host="localhost", user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], port=3306)
cur = db.cursor()
cur.execute("SELECT * FROM states")
rw = cur.fetchall()
for row in rw:
    print(row)
cur.close()
db.close()
