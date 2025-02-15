import sqlite3
import json

# Load JSON data
with open('updated_process.json', 'r') as file:
    data = json.load(file)

# Connect to SQLite database (or create it)
conn = sqlite3.connect('mobile_money.db')
cursor = conn.cursor()

# Function to handle missing keys
def get_value(entry, key):
    return entry.get(key, 'N/a')  # Return 'N/a' if key is missing

# Create tables
cursor.execute('''
CREATE TABLE IF NOT EXISTS IncomingMoney (
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
CREATE TABLE IF NOT EXISTS PaymentsToCodeHolders (
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
CREATE TABLE IF NOT EXISTS TransfersToMobileNumbers (
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
CREATE TABLE IF NOT EXISTS BankDeposits (
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
CREATE TABLE IF NOT EXISTS AirtimeBillPayments (
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
CREATE TABLE IF NOT EXISTS CashPowerBillPayments (
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
CREATE TABLE IF NOT EXISTS TransactionsInitiatedbyThirdParties (
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
CREATE TABLE IF NOT EXISTS WithdrawalsfromAgents (
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
CREATE TABLE IF NOT EXISTS BankTransfers (
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
CREATE TABLE IF NOT EXISTS InternetAndVoiceBundlePurchases (
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
    INSERT INTO IncomingMoney (contact_name, address, date_sent, readable_date, body, service_center, amount, sender, new_balance)
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
for entry in data.get('Payments_to_Code_Holderss', []):
    cursor.execute('''
    INSERT INTO PaymentsToCodeHolders (contact_name, address, date_sent, readable_date, body, service_center, amount, recipient, new_balance)
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
    INSERT INTO TransfersToMobileNumbers (contact_name, address, date_sent, readable_date, body, service_center, amount, recipient, new_balance)
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
    INSERT INTO BankDeposits (contact_name, address, date_sent, readable_date, body, service_center, amount, recipient, new_balance)
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
    INSERT INTO AirtimeBillPayments (contact_name, address, date_sent, readable_date, body, service_center, amount, recipient, new_balance)
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
    INSERT INTO CashPowerBillPayments (contact_name, address, date_sent, readable_date, body, service_center, amount, recipient, new_balance)
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
for entry in data.get('Transactions_Initiated_by_Third Parties', []):
    cursor.execute('''
    INSERT INTO TransactionsInitiatedbyThirdParties (contact_name, address, date_sent, readable_date, body, service_center, amount, recipient, new_balance)
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
    INSERT INTO WithdrawalsfromAgents (contact_name, address, date_sent, readable_date, body, service_center, amount, recipient, new_balance)
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
    INSERT INTO BankTransfers (contact_name, address, date_sent, readable_date, body, service_center, amount, recipient, new_balance)
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
    INSERT INTO InternetAndVoiceBundlePurchases (contact_name, address, date_sent, readable_date, body, service_center, amount, recipient, new_balance)
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

# Commit changes and close the connection
conn.commit()
conn.close()

print("Database created and data inserted successfully.")