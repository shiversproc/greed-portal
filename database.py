import sqlite3
from sqlalchemy import create_engine
engine = create_engine("sqlite:///database.db", echo=True)

try:
    with sqlite3.connect("database.db") as conn:
        print(conn)
except sqlite3.OperationalError as e:
    print(e)
