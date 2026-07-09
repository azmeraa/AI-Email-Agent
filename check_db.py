import sqlite3

conn = sqlite3.connect('email_agent.db')
cursor = conn.cursor()
cursor.execute('SELECT id, sender, subject FROM emails')
rows = cursor.fetchall()

print("Current entries in database:")
for row in rows:
    print(row)

conn.close()