import sqlite3


def connect():
    return sqlite3.connect("data/app.db")


def create_tables():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT,
        password TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY,
        task TEXT,
        done INTEGER,
        user_id INTEGER
    )
    """)

    conn.commit()
    conn.close()
