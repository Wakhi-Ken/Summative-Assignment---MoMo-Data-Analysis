from flask import Flask, jsonify, render_template, request
import logging
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
@app.route('/analytics')
def analytics():
    return render_template('analytics.html')


# Function to fetch all transactions
def get_transactions():
    conn = sqlite3.connect('database/balances.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Balances')
    transactions = cursor.fetchall()
    conn.close()
    return transactions
# Route to fetch all transactions
@app.route('/api/transactions')
def transactions():
    transactions = get_transactions()
    return jsonify(transactions) 


# Function to fetch all messages for a specific transaction type
def get_messages(table_name):
    print(f"get_messages called with table_name: {table_name}")

    allowed_tables = {"Incoming_Money", "Payments_To_Code_Holders", "Transfers_to_Mobile_Numbers", "Bank_Deposits", "Airtime_Bill_Payments", "Cash_Power_Bill_Payments", "Transactions_Initiated_by_Third_Parties", "Withdrawals_from_Agents", "Bank_Transfers", "Internet_And_Voice_Bundle_Purchases", "Other"}
    if table_name not in allowed_tables:
        print("Invalid table name")
        return []

    try:
        with sqlite3.connect('database/mobile_money.db') as conn:
            cursor = conn.cursor()
            query = f"SELECT * FROM {table_name} LIMIT 9"  # Select all columns
            cursor.execute(query)
            
            # Fetch all rows and convert them into dictionaries
            rows = cursor.fetchall()
            columns = [column[0] for column in cursor.description]
            messages = [dict(zip(columns, row)) for row in rows]

            print(f"Messages fetched: {messages}")
            return messages

    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []  # Return empty list on DB error
    except Exception as e:
        print(f"Unexpected error: {e}")
        return []
# Route to fetch all messages for a specific transaction type    
@app.route('/api/mobile_money')
def mobile_money():
    transaction_type = request.args.get('table_name')

    if not transaction_type:
        return jsonify({'error': 'Table name is required'}), 400

    messages = get_messages(transaction_type)
    return jsonify({'tmessages': messages})

# Function to fetch the total amount for a specific transaction type
def get_total_amount_by_type(transaction_type):
    try:
        with sqlite3.connect('database/balances.db') as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT amount FROM Balances WHERE transaction_type = ?', (transaction_type,))
            result = cursor.fetchone()
            if result:
                return result[0]
            else:
                return 0
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return 0
    except Exception as e:
        print(f"Error: {e}")
        return 0
# Route to fetch the total amount for a specific transaction type   
@app.route('/api/total_amount')
def total_amount():
    transaction_type = request.args.get('transaction_type')
    if not transaction_type:
        return jsonify({'error': 'Transaction type is required'}), 400
    total_amount = get_total_amount_by_type(transaction_type)
    return jsonify({'transaction_type': transaction_type, 'total_amount': total_amount})


# Function to fetch all messages for all transaction types
def get_messages_from_database(table_name):
    print(f"get_messages_from_database called with table_name: {table_name}")

    allowed_tables = {"Incoming_Money", "Payments_To_Code_Holders", "Transfers_to_Mobile_Numbers", 
                      "Bank_Deposits", "Airtime_Bill_Payments", "Cash_Power_Bill_Payments", 
                      "Transactions_Initiated_by_Third_Parties", "Withdrawals_from_Agents", 
                      "Bank_Transfers", "Internet_And_Voice_Bundle_Purchases", "Other"}

    if table_name not in allowed_tables:
        print(f"Table '{table_name}' is not in allowed_tables.")
        return []

    try:
        with sqlite3.connect('database/mobile_money.db') as conn:
            cursor = conn.cursor()

            print(f"Fetching data from table: {table_name}")
            query = f"SELECT * FROM {table_name}" 
            cursor.execute(query)

            rows = cursor.fetchall()
            columns = [column[0] for column in cursor.description]
            messages = [dict(zip(columns, row)) for row in rows]

            print(f"Fetched {len(messages)} messages from table {table_name}")
            return messages

    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return [] 
    except Exception as e:
        print(f"Unexpected error: {e}")
        return []
# Route to fetch all messages for all transaction types
@app.route('/api/messages')
def get_tables():
    print("in /api/messages")
    logging.debug("Entering /api/messages route handler")

    table_names = ["Incoming_Money", "Payments_To_Code_Holders", "Transfers_to_Mobile_Numbers", 
                  "Bank_Deposits", "Airtime_Bill_Payments", "Cash_Power_Bill_Payments", 
                  "Transactions_Initiated_by_Third_Parties", "Withdrawals_from_Agents", 
                   "Bank_Transfers", "Internet_And_Voice_Bundle_Purchases", "Other"]

    logging.debug(f"Retrieved table names: {table_names}")

    response_object = {"tables": table_names}

    logging.debug(f"Response object before jsonify: {response_object}")

    return jsonify(response_object)

def fetch_messages_from_table(table_name):
    print(f"fetch_messages_from_table called with table_name: {table_name}")

    allowed_tables = {"Incoming_Money", "Payments_To_Code_Holders", "Transfers_to_Mobile_Numbers", 
                      "Bank_Deposits", "Airtime_Bill_Payments", "Cash_Power_Bill_Payments", 
                      "Transactions_Initiated_by_Third_Parties", "Withdrawals_from_Agents", 
                      "Bank_Transfers", "Internet_And_Voice_Bundle_Purchases", "Other"}

    if table_name not in allowed_tables:
        print(f"Table '{table_name}' is not in allowed_tables.")
        return []

    try:
        with sqlite3.connect('database/mobile_money.db') as conn:
            cursor = conn.cursor()

            print(f"Fetching data from table: {table_name}")
            query = f"SELECT * FROM {table_name}" 
            cursor.execute(query)

            rows = cursor.fetchall()
            columns = [column[0] for column in cursor.description]
            messages = [dict(zip(columns, row)) for row in rows]

            print(f"Fetched {len(messages)} messages from table {table_name}")
            return messages

    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return [] 
    except Exception as e:
        print(f"Unexpected error: {e}")
        return []

# Route to fetch all messages from all transaction tables
@app.route('/api/all_messages')
def fetch_all_messages():
    print("in /api/all_messages")
    logging.debug("Entering /api/all_messages route handler")

    table_names = ["Incoming_Money", "Payments_To_Code_Holders", "Transfers_to_Mobile_Numbers", 
                  "Bank_Deposits", "Airtime_Bill_Payments", "Cash_Power_Bill_Payments", 
                  "Transactions_Initiated_by_Third_Parties", "Withdrawals_from_Agents", 
                  "Bank_Transfers", "Internet_And_Voice_Bundle_Purchases", "Other"]

    logging.debug(f"Retrieved table names: {table_names}")

    all_messages = {}

    for table in table_names:
        all_messages[table] = fetch_messages_from_table(table)

    logging.debug(f"Response object before jsonify: {all_messages}")

    return jsonify(all_messages)



def get_balances():
    conn = sqlite3.connect("database/balances.db")
    cursor = conn.cursor()
    cursor.execute("SELECT transaction_type, amount FROM Balances")
    data = cursor.fetchall()
    conn.close()
    return [{"transaction_type": row[0], "amount": row[1]} for row in data]

@app.route("/balances", methods=["GET"])
def balances():
    return jsonify(get_balances())



if __name__ == '__main__':
    app.run(debug=True)