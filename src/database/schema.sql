CREATE TABLE IF NOT EXISTS transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    transaction_id TEXT UNIQUE,
    transaction_type TEXT NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    transaction_date DATETIME NOT NULL,
    sender_info TEXT,
    recipient_info TEXT,
    description TEXT,
    status TEXT DEFAULT 'completed',
    raw_message TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT unique_transaction UNIQUE (transaction_id, transaction_date)
);

CREATE INDEX IF NOT EXISTS idx_transaction_date ON transactions(transaction_date);
CREATE INDEX IF NOT EXISTS idx_transaction_type ON transactions(transaction_type);
