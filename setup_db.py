import sqlite3

# Connect to (or create) the database
conn = sqlite3.connect('customer_data.db')
cursor = conn.cursor()

# Create table
cursor.execute('''CREATE TABLE IF NOT EXISTS customers 
                  (name TEXT, email TEXT, status TEXT)''')

# Insert sample data
sample_data = [
    ('Abebe Teshale', 'abebe@example.com', 'active'),
    ('Sara Kebede', 'sara@example.com', 'inactive'),
    ('Tech User', 'user@example.com', 'active')
]

cursor.executemany('INSERT INTO customers VALUES (?,?,?)', sample_data)
conn.commit()
conn.close()

print("Database created successfully with sample data!")