import sqlite3

def init_db():
    conn = sqlite3.connect('email_agent.db')
    cursor = conn.cursor()
    
    # Create table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS emails (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sender TEXT,
            subject TEXT,
            received_date TIMESTAMP,
            body TEXT,
            category TEXT,
            is_processed INTEGER DEFAULT 0
        )
    ''')
    
    conn.commit()
    conn.close()
    print("Database and table 'emails' initialized successfully.")

if __name__ == "__main__":
    init_db()