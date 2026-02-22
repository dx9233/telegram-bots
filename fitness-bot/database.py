import sqlite3


def connect():
    return sqlite3.connect("clients.db")


def create_tables():
    db = connect()
    cur = db.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS clients (
        id INTEGER PRIMARY KEY,
        tg_id INTEGER,
        name TEXT,
        phone TEXT
    )
    """)

    db.commit()
    db.close()


def add_client(tg_id, name, phone):
    db = connect()
    cur = db.cursor()

    cur.execute("""
    INSERT INTO clients (tg_id, name, phone)
    VALUES (?, ?, ?)
    """, (tg_id, name, phone))

    db.commit()
    db.close()