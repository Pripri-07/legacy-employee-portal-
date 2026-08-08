import os
import sqlite3

DB_PATH = "database/employee.db"
SQL_PATH = "database/init.sql"

if os.path.exists(DB_PATH):
    os.remove(DB_PATH)

connection = sqlite3.connect(DB_PATH)

with open(SQL_PATH, "r") as sql_file:
    sql_script = sql_file.read()

connection.executescript(sql_script)

connection.commit()
connection.close()

print("Database initialized successfully!")