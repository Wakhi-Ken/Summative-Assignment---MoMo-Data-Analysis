import sqlite3
import json

# Load JSON data from balances.json
with open('balances.json', 'r') as file:
    data = json.load(file)

# Connect to SQLite database (or create it)
conn = sqlite3.connect('balances.db')
cursor = conn.cursor()

# Create a table to store the balances(totals)
cursor.execute('''
CREATE TABLE IF NOT EXISTS Balances (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    transaction_type TEXT UNIQUE,
    amount REAL
)
''')

# Insert data into the Balances table
for transaction_type, amount in data.items():
    cursor.execute('''
    INSERT OR REPLACE INTO Balances (transaction_type, amount)
    VALUES (?, ?)
    ''', (transaction_type, amount))

conn.commit()
conn.close()

print("Database created and data inserted successfully.")