import sqlite3

DB_PATH = "pantry.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS pantry (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            quantity REAL,
            unit TEXT,
            expiry TEXT
        )
    """)
    conn.commit()
    conn.close()

def get_ingredients():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT * FROM pantry")
    rows = c.fetchall()
    conn.close()
    return rows

def add_ingredient(name, quantity, unit, expiry):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("INSERT INTO pantry (name, quantity, unit, expiry) VALUES (?, ?, ?, ?)",
              (name, quantity, unit, expiry))
    conn.commit()
    conn.close()



