# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 16:28:16 2022
Data store sql db
@author: Calvin
"""

import sqlite3

#conn is main link to the database
conn = sqlite3.connect("Names.db")

conn.execute("CREATE TABLE IF NOT EXISTS PERSON_NAMES(FIRSTNAME TEXT, MIDDLENAME TEXT, LASTNAME TEXT, AGE INT)")

print("Table created sucessfully")

conn.execute("INSERT INTO PERSON_NAMES(FIRSTNAME, MIDDLENAME, LASTNAME, AGE) VALUES('Stalin', 'R', 'Rodrigues', '23')")
conn.execute("INSERT INTO PERSON_NAMES(FIRSTNAME, MIDDLENAME, LASTNAME, AGE) VALUES('Calvin', 'S', 'Rodrigues', '23')")
#cusrsor for select query
cur = conn.cursor()
#using cursor execute the select statement
cur.execute("SELECT * FROM PERSON_NAMES")

#get all data from table and print it
table_data = cur.fetchall()
for record in table_data:
    print(record)
