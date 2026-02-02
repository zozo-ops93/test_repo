import sqlite3

conn = sqlite3.connect("crypto.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS prices(
    coin TEXT,
    price REAL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
""")