import os
from dotenv import load_dotenv

import mysql.connector as conn

load_dotenv()

my_db = conn.connect(
    # host = os.getenv("DB_HOST"),
    host = 'localhost',
    user = 'root',
    password = 'jesus4life'
)

# print(my_db)

my_cursor = my_db.cursor()

# Create a database
my_cursor.execute('CREATE DATABASE cen434_live')
my_cursor.execute('USE cen434_live')

# Create table
my_cursor.execute("CREATE TABLE students (name VARCHAR(255), matno VARCHAR(255))")

# Add data
sql = "INSERT INTO students (name, matno) VALUES (%s, %s)"
val = ("Kathy", "20cj027xxx")
my_cursor.execute(sql, val)

my_db.commit()

print(my_cursor.rowcount, "record inserted.")

# Read data
my_cursor.execute("SELECT name, matno FROM students")

myresult = my_cursor.fetchall()

for x in myresult:
  print(x)

# Update data
sql = "UPDATE students SET matno = '20CJ028xxx' WHERE matno = '20CJ027xxx'"

my_cursor.execute(sql)

my_db.commit()

print(my_cursor.rowcount, "record(s) affected")

# Delete data
sql = "DELETE FROM students WHERE matno = '20cj027xxx'"

my_cursor.execute(sql)

my_db.commit()

print(my_cursor.rowcount, "record(s) deleted")

# Delete table
sql = "DROP TABLE students"

my_cursor.execute(sql)

# Delete database
sql = "DROP DATABASE cen434_live"

my_cursor.execute(sql)


# close connection
my_db.close()