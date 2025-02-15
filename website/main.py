from flask import Flask, jsonify, render_template, request
import sqlite3
app = Flask(__name__)

# Routes to serve the HTML pages
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/details')
def details():
    return render_template('details.html')

# Function to fetch all transactions
def get_transactions():
    conn = sqlite3.connect('database/balances.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Balances')
    transactions = cursor.fetchall()
    conn.close()
    return transactions

def get_messages(transaction_type):
    valid_tables = ['Incoming_Money', 'Payments_to_Code_Holders', 'Transfers_to_Mobile_Numbers', 'Bank_Deposits', 'Airtime_Bill_Payments', 'Cash_Power_Bill_Payments', 'Transactions_Initiated_by_Third Parties', 'Withdrawals_from_Agents', 'Bank_Transfers', 'Internet_and_Voice_Bundle_Purchases', 'Others']
    query = f'SELECT * FROM {transaction_type}'
    conn = sqlite3.connect('database/mobile_money.db')
    cursor = conn.cursor()
    cursor.execute(query)
    mobile_money = cursor.fetchall()
    conn.close()
    return mobile_money

# Function to fetch the total amount for a specific transaction type
def get_total_amount_by_type(transaction_type):
    conn = sqlite3.connect('database/balances.db')
    cursor = conn.cursor()
    cursor.execute('SELECT SUM(amount) FROM Balances WHERE transaction_type = ?', (transaction_type,))
    total_amount = cursor.fetchone()[0] 
    conn.close()
    return total_amount or 0

# Route to fetch all transactions as JSON
@app.route('/api/transactions')
def transactions():
    transactions = get_transactions()
    return jsonify(transactions)

# Route to fetch the total amount for a specific transaction type
@app.route('/api/total_amount')
def total_amount():
    transaction_type = request.args.get('type')
    if not transaction_type:
        return jsonify({'error': 'Transaction type is required'}), 400
    total_amount = get_total_amount_by_type(transaction_type)
    return jsonify({'transaction_type': transaction_type, 'total_amount': total_amount})

if __name__ == '__main__':
    app.run(debug=True)