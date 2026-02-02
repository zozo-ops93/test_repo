import requests
import sqlite3
import time

conn = sqlite3.connect("crypto.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS prices(
    coin TEXT,
    price REAL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
""")
conn.commit()

while True:
    url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
    data = requests.get(url).json()
    
    price = float(data["price"])
    
    cursor.execute("INSERT INTO prices VALUES (?, ?, datetime('now'))",
                   ("bitcoin", price))
    conn.commit()
    
    print("Inserted:", price)
    time.sleep(10)   # every 10 seconds
