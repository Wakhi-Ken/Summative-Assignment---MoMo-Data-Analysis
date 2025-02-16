import unittest
import os
import sqlite3
from src.database import MoMoDatabase

class TestMoMoDatabase(unittest.TestCase):
    def setUp(self):
        """Set up a test database before each test"""
        self.test_db_file = "test_momo_transactions.db"
        self.db = MoMoDatabase(self.test_db_file)

    def tearDown(self):
        """Clean up test database after each test"""
        if os.path.exists(self.test_db_file):
            os.remove(self.test_db_file)

    def test_insert_transaction(self):
        """Test inserting a single transaction"""
        test_transaction = {
            'transaction_id': 'TEST123',
            'transaction_type': 'MONEY_RECEIVED',
            'amount': 5000.00,
            'transaction_date': '2024-02-13 10:00:00',
            'sender_name': 'Test Sender',
            'raw_message': 'Test message'
        }
        
        # Test insertion
        result = self.db.insert_transaction(test_transaction)
        self.assertTrue(result)

        # Verify insertion
        with sqlite3.connect(self.test_db_file) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT transaction_id FROM transactions WHERE transaction_id = ?", 
                         (test_transaction['transaction_id'],))
            result = cursor.fetchone()
            self.assertIsNotNull(result)
