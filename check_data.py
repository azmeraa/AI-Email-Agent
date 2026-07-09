import sqlite3

# Connect to the exact database file
db_path = r'E:\Email_Agent_Project\email_agent.db'
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Check how many emails are in the table
cursor.execute("SELECT COUNT(*) FROM emails")
count = cursor.fetchone()[0]
print(f"Total emails currently in database: {count}")

# Show the categories for the first 5 emails
cursor.execute("SELECT subject, category FROM emails LIMIT 5")
rows = cursor.fetchall()
for row in rows:
    print(f"Subject: {row[0]} | Category: {row[1]}")

conn.close()