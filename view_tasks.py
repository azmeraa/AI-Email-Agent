import sqlite3
conn = sqlite3.connect('email_agent.db')
cursor = conn.cursor()
cursor.execute('SELECT task_description, due_date, priority FROM tasks')
for task in cursor.fetchall():
    print(f"Task: {task[0]} | Due: {task[1]} | Priority: {task[2]}")
conn.close()