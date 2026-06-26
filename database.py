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
    """CREATE TABLE IF NOT EXISTS Holdings (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        ticker_symbol TEXT NOT NULL,
        stock_name TEXT NOT NULL,
        holding_amount INTEGER NOT NULL,
        gains/losses INTEGER NOT NULL,
        total_gains INTEGER NOT NULL,
        RSI INTEGER NOT NULL,
        SMA_20 INTEGER NOT NULL,
        SMA_50 INTEGER NOT NULL,);
        """,
    """CREATE TABLE IF NOT EXISTS Indicators (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    ticker_symbol TEXT NOT NULL,
    stock_name TEXT NOT NULL,
    RSI INTEGER NOT NULL,
    SMA_20 INTEGER NOT NULL,
    SMA_50 INTEGER NOT NULL,
    """
]


def create_table (database, statements=table_statements ):

    try:
        with sqlite3.connect(f"{database}") as conn:
            cursor = conn.cursor()
            for statement in table_statements:
                cursor.execute(statement)
            conn.commit()
            print(f"Tables created")
            return

    except sqlite3.OperationalError as e:
        print("Failed to create tables.", e)
        return