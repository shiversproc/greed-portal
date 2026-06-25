import sqlite3
from sqlalchemy import create_engine
engine = create_engine("sqlite:///database.db", echo=True)


def connect_db():
    try:
        with sqlite3.connect("database.db") as conn:
            print(conn)
            return
    except sqlite3.OperationalError as e:
        print(e)
        return


table_statements = [

]


def create_table (database, table_name):

    try:
        with sqlite3.connect(f"{database}") as conn:
            cursor = conn.cursor()
            cursor.execute(f"{table_name}")
            conn.commit()
            return

    except sqlite3.OperationalError as e:
        print(e)
        return