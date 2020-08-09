import sqlite3
from sqlite3 import Error


# Establishes a connection to the database, returns it in 'conn'.
def connect(db_file):
    conn = None

    try:
        conn = sqlite3.connect(db_file)
        print("SQLite3 Version " + sqlite3.version)
    except Error as e:
        print("Error: " + str(e))

    return conn


# Path to the database object.
database = r"C:\sqlite\db\wheel.db"

# Creates a connection to the database with the 'conn' variable, and places the SQL cursor
# into the 'c' variable.
conn = connect(database)
c = conn.cursor()
