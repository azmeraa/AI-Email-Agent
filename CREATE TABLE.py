import sqlite3
conn = sqlite3.connect('email_agent.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email_id INTEGER,
        task_description TEXT,
        due_date TEXT,
        priority TEXT,
        status TEXT DEFAULT 'Pending',
        FOREIGN KEY (email_id) REFERENCES emails(id)
    )
''')
conn.commit()
conn.close()
print("Table 'tasks' is ready.")