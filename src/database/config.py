import os

# Database configuration
DB_FILE = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 
                      'momo_transactions.db')

# Transaction types mapping
TRANSACTION_TYPES = {
    'MONEY_RECEIVED': 'incoming_money',
    'PAYMENT_TO_MERCHANT': 'payments',
    'TRANSFER_TO_MOBILE': 'transfer',
    'BANK_DEPOSIT': 'deposit',
    'AIRTIME_PURCHASE': 'airtime',
    'CASH_POWER': 'cash_power',
    'THIRD_PARTY': 'third_party',
    'AGENT_WITHDRAWAL': 'withdraw',
    'BUNDLE_PURCHASE': 'bundles'
}
