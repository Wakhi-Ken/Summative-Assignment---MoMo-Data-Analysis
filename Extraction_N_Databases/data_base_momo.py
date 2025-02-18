import sqlite3
import json

# Load JSON data
with open('updated_process.json', 'r') as file:
    data = json.load(file)

# Connect to SQLite database (or create it)
conn = sqlite3.connect('mobile_money.db')
cursor = conn.cursor()

# Function to handle missing keys and return 'N/a' if key is missing
def get_value(entry, key):
    return entry.get(key, 'N/a')

# Create tables
cursor.execute('''
CREATE TABLE IF NOT EXISTS Incoming_Money (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    contact_name TEXT,
    address TEXT,
    date_sent TEXT,
    readable_date TEXT,
    body TEXT,
    service_center TEXT,
    amount TEXT,
    sender TEXT,
    new_balance TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Payments_To_Code_Holders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    contact_name TEXT,
    address TEXT,
    date_sent TEXT,
    readable_date TEXT,
    body TEXT,
    service_center TEXT,
    amount TEXT,
    recipient TEXT,
    new_balance TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Transfers_To_Mobile_Numbers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    contact_name TEXT,
    address TEXT,
    date_sent TEXT,
    readable_date TEXT,
    body TEXT,
    service_center TEXT,
    amount TEXT,
    recipient TEXT,
    new_balance TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Bank_Deposits (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    contact_name TEXT,
    address TEXT,
    date_sent TEXT,
    readable_date TEXT,
    body TEXT,
    service_center TEXT,
    amount TEXT,
    recipient TEXT,
    new_balance TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Airtime_Bill_Payments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    contact_name TEXT,
    address TEXT,
    date_sent TEXT,
    readable_date TEXT,
    body TEXT,
    service_center TEXT,
    amount TEXT,
    recipient TEXT,
    new_balance TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Cash_Power_Bill_Payments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    contact_name TEXT,
    address TEXT,
    date_sent TEXT,
    readable_date TEXT,
    body TEXT,
    service_center TEXT,
    amount TEXT,
    recipient TEXT,
    new_balance TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Transactions_Initiated_by_Third_Parties (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    contact_name TEXT,
    address TEXT,
    date_sent TEXT,
    readable_date TEXT,
    body TEXT,
    service_center TEXT,
    amount TEXT,
    recipient TEXT,
    new_balance TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Withdrawals_from_Agents (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    contact_name TEXT,
    address TEXT,
    date_sent TEXT,
    readable_date TEXT,
    body TEXT,
    service_center TEXT,
    amount TEXT,
    recipient TEXT,
    new_balance TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Bank_Transfers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    contact_name TEXT,
    address TEXT,
    date_sent TEXT,
    readable_date TEXT,
    body TEXT,
    service_center TEXT,
    amount TEXT,
    recipient TEXT,
    new_balance TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Internet_And_Voice_Bundle_Purchases (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    contact_name TEXT,
    address TEXT,
    date_sent TEXT,
    readable_date TEXT,
    body TEXT,
    service_center TEXT,
    amount TEXT,
    recipient TEXT,
    new_balance TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Other (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    contact_name TEXT,
    address TEXT,
    date_sent TEXT,
    readable_date TEXT,
    body TEXT,
    service_center TEXT,
    amount TEXT,
    recipient TEXT,
    new_balance TEXT
)
''')

# Insert data into IncomingMoney
for entry in data.get('Incoming_Money', []):
    cursor.execute('''
    INSERT INTO Incoming_Money (contact_name, address, date_sent, readable_date, body, service_center, amount, sender, new_balance)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        get_value(entry, 'contact_name'),
        get_value(entry, 'address'),
        get_value(entry, 'date_sent'),
        get_value(entry, 'readable_date'),
        get_value(entry, 'body'),
        get_value(entry, 'service_center'),
        get_value(entry, 'amount'),
        get_value(entry, 'sender'),
        get_value(entry, 'new_balance')
    ))

# Insert data into PaymentsToCodeHolders
for entry in data.get('Payments_to_Code_Holders', []):
    cursor.execute('''
    INSERT INTO Payments_to_Code_Holders (contact_name, address, date_sent, readable_date, body, service_center, amount, recipient, new_balance)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        get_value(entry, 'contact_name'),
        get_value(entry, 'address'),
        get_value(entry, 'date_sent'),
        get_value(entry, 'readable_date'),
        get_value(entry, 'body'),
        get_value(entry, 'service_center'),
        get_value(entry, 'amount'),
        get_value(entry, 'recipient'),
        get_value(entry, 'new_balance')
    ))

# Insert data into TransfersToMobileNumbers
for entry in data.get('Transfers_to_Mobile_Numbers', []):
    cursor.execute('''
    INSERT INTO Transfers_to_Mobile_Numbers (contact_name, address, date_sent, readable_date, body, service_center, amount, recipient, new_balance)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        get_value(entry, 'contact_name'),
        get_value(entry, 'address'),
        get_value(entry, 'date_sent'),
        get_value(entry, 'readable_date'),
        get_value(entry, 'body'),
        get_value(entry, 'service_center'),
        get_value(entry, 'amount'),
        get_value(entry, 'recipient'),
        get_value(entry, 'new_balance')
    ))

# Insert data into BankDeposits
for entry in data.get('Bank_Deposits', []):
    cursor.execute('''
    INSERT INTO Bank_Deposits (contact_name, address, date_sent, readable_date, body, service_center, amount, recipient, new_balance)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        get_value(entry, 'contact_name'),
        get_value(entry, 'address'),
        get_value(entry, 'date_sent'),
        get_value(entry, 'readable_date'),
        get_value(entry, 'body'),
        get_value(entry, 'service_center'),
        get_value(entry, 'amount'),
        get_value(entry, 'recipient'),
        get_value(entry, 'new_balance')
    ))

# Insert data into AirtimeBillPayments
for entry in data.get('Airtime_Bill_Payments', []):
    cursor.execute('''
    INSERT INTO Airtime_Bill_Payments (contact_name, address, date_sent, readable_date, body, service_center, amount, recipient, new_balance)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        get_value(entry, 'contact_name'),
        get_value(entry, 'address'),
        get_value(entry, 'date_sent'),
        get_value(entry, 'readable_date'),
        get_value(entry, 'body'),
        get_value(entry, 'service_center'),
        get_value(entry, 'amount'),
        get_value(entry, 'recipient'),
        get_value(entry, 'new_balance')
    ))

# Insert data into CashPowerBillPayments
for entry in data.get('Cash_Power_Bill_Payments', []):
    cursor.execute('''
    INSERT INTO Cash_Power_Bill_Payments (contact_name, address, date_sent, readable_date, body, service_center, amount, recipient, new_balance)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        get_value(entry, 'contact_name'),
        get_value(entry, 'address'),
        get_value(entry, 'date_sent'),
        get_value(entry, 'readable_date'),
        get_value(entry, 'body'),
        get_value(entry, 'service_center'),
        get_value(entry, 'amount'),
        get_value(entry, 'recipient'),
        get_value(entry, 'new_balance')
    ))

# Insert data into TransactionsInitiatedbyThirdParties
for entry in data.get('Transactions_Initiated_by_Third_Parties', []):
    cursor.execute('''
    INSERT INTO Transactions_Initiated_by_Third_Parties (contact_name, address, date_sent, readable_date, body, service_center, amount, recipient, new_balance)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        get_value(entry, 'contact_name'),
        get_value(entry, 'address'),
        get_value(entry, 'date_sent'),
        get_value(entry, 'readable_date'),
        get_value(entry, 'body'),
        get_value(entry, 'service_center'),
        get_value(entry, 'amount'),
        get_value(entry, 'recipient'),
        get_value(entry, 'new_balance')
    ))

# Insert data into WithdrawalsfromAgents
for entry in data.get('Withdrawals_from_Agents', []):
    cursor.execute('''
    INSERT INTO Withdrawals_from_Agents (contact_name, address, date_sent, readable_date, body, service_center, amount, recipient, new_balance)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        get_value(entry, 'contact_name'),
        get_value(entry, 'address'),
        get_value(entry, 'date_sent'),
        get_value(entry, 'readable_date'),
        get_value(entry, 'body'),
        get_value(entry, 'service_center'),
        get_value(entry, 'amount'),
        get_value(entry, 'recipient'),
        get_value(entry, 'new_balance')
    ))

# Insert data into BankTransfers
for entry in data.get('Bank_Transfers', []):
    cursor.execute('''
    INSERT INTO Bank_Transfers (contact_name, address, date_sent, readable_date, body, service_center, amount, recipient, new_balance)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        get_value(entry, 'contact_name'),
        get_value(entry, 'address'),
        get_value(entry, 'date_sent'),
        get_value(entry, 'readable_date'),
        get_value(entry, 'body'),
        get_value(entry, 'service_center'),
        get_value(entry, 'amount'),
        get_value(entry, 'recipient'),
        get_value(entry, 'new_balance')
    ))

# Insert data into InternetAndVoiceBundlePurchases
for entry in data.get('Internet_and_Voice_Bundle_Purchases', []):
    cursor.execute('''
    INSERT INTO Internet_and_Voice_Bundle_Purchases (contact_name, address, date_sent, readable_date, body, service_center, amount, recipient, new_balance)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        get_value(entry, 'contact_name'),
        get_value(entry, 'address'),
        get_value(entry, 'date_sent'),
        get_value(entry, 'readable_date'),
        get_value(entry, 'body'),
        get_value(entry, 'service_center'),
        get_value(entry, 'amount'),
        get_value(entry, 'recipient'),
        get_value(entry, 'new_balance')
    ))

# Insert data into Other
for entry in data.get('Other', []):
    cursor.execute('''
    INSERT INTO Other (contact_name, address, date_sent, readable_date, body, service_center, amount, recipient, new_balance)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        get_value(entry, 'contact_name'),
        get_value(entry, 'address'),
        get_value(entry, 'date_sent'),
        get_value(entry, 'readable_date'),
        get_value(entry, 'body'),
        get_value(entry, 'service_center'),
        get_value(entry, 'amount'),
        get_value(entry, 'recipient'),
        get_value(entry, 'new_balance')
    ))

conn.commit()
conn.close()

print("Database created and data inserted successfully.")