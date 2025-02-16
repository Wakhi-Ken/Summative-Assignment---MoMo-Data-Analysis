import sqlite3
import logging
from datetime import datetime
from typing import Dict, Any, List, Tuple
import os
from .config import DB_FILE

class MoMoDatabase:
    def __init__(self, db_file: str = DB_FILE):
        """Initialize database connection and setup"""
        self.db_file = db_file
        self.setup_logging()
        self.initialize_database()
    
    def setup_logging(self):
        """Configure logging for database operations"""
        log_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'logs')
        os.makedirs(log_dir, exist_ok=True)
        
        logging.basicConfig(
            filename=os.path.join(log_dir, 'database_operations.log'),
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger(__name__)

    def initialize_database(self):
        """Create database tables if they don't exist"""
        try:
            with sqlite3.connect(self.db_file) as conn:
                with open(os.path.join(os.path.dirname(__file__), 'schema.sql'), 'r') as schema_file:
                    conn.executescript(schema_file.read())
            self.logger.info("Database initialized successfully")
        except Exception as e:
            self.logger.error(f"Failed to initialize database: {str(e)}")
            raise

    def insert_transaction(self, transaction_data: Dict[str, Any]) -> bool:
        """Insert a single transaction into the database"""
        try:
            with sqlite3.connect(self.db_file) as conn:
                cursor = conn.cursor()
                
                # Check for duplicate transaction_id
                if transaction_data.get('transaction_id'):
                    cursor.execute(
                        "SELECT COUNT(*) FROM transactions WHERE transaction_id = ?",
                        (transaction_data['transaction_id'],)
                    )
                    if cursor.fetchone()[0] > 0:
                        self.logger.warning(f"Duplicate transaction_id: {transaction_data['transaction_id']}")
                        return False

                # Prepare insertion query
                columns = ', '.join(transaction_data.keys())
                placeholders = ', '.join(['?' for _ in transaction_data])
                query = f"INSERT INTO transactions ({columns}) VALUES ({placeholders})"
                
                cursor.execute(query, list(transaction_data.values()))
                self.logger.info(f"Successfully inserted transaction: {transaction_data.get('transaction_id')}")
                return True
                
        except sqlite3.Error as e:
            self.logger.error(f"Database error: {str(e)}")
            self.log_failed_transaction(transaction_data, str(e))
            return False

