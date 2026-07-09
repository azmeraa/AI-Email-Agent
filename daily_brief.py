import sqlite3
import os
from datetime import datetime

def show_daily_briefing():
    db_path = r'E:\Email_Agent_Project\email_agent.db'
    if not os.path.exists(db_path):
        print(f"Error: Database file not found at {db_path}")
        return

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    print(f"--- Daily Briefing: {datetime.now().strftime('%Y-%m-%d')} ---")
    
    # 1. High Priority List
    cursor.execute("SELECT task_description FROM tasks WHERE priority = 'High' AND status = 'Pending'")
    high_tasks = cursor.fetchall()
    print("\n[!] HIGH PRIORITY TASKS:")
    for task in high_tasks:
        print(f"- {task[0]}")

    # 2. Medium Priority List (Added)
    cursor.execute("SELECT task_description FROM tasks WHERE priority = 'Medium' AND status = 'Pending'")
    med_tasks = cursor.fetchall()
    print("\n[ ] MEDIUM PRIORITY TASKS:")
    for task in med_tasks:
        print(f"- {task[0]}")

    # 3. Workload Summary
    cursor.execute("SELECT priority, COUNT(*) FROM tasks WHERE status = 'Pending' GROUP BY priority")
    summary = cursor.fetchall()
    print("\n--- WORKLOAD SUMMARY ---")
    for item in summary:
        print(f"- {item[0] or 'Not Specified'}: {item[1]} tasks")
            
    conn.close()

if __name__ == "__main__":
    show_daily_briefing()