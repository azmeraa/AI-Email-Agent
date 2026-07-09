import sqlite3
import json
import requests
import os

def extract_tasks_from_db():
    # Ensure we are using the absolute path to the database
    db_path = r'E:\Email_Agent_Project\email_agent.db'
    if not os.path.exists(db_path):
        print(f"Error: Database file not found at {db_path}")
        return

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # 1. Schema Validation: Ensure 'tasks' table exists
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
    
    # 2. Fetch emails that are categorized
    cursor.execute("SELECT id, subject, body FROM emails WHERE category != 'Uncategorized'")
    emails = cursor.fetchall()
    
    if not emails:
        print("No categorized emails found to analyze.")
        conn.close()
        return

    for email in emails:
        # Check if this email already has a task to prevent duplicates
        cursor.execute("SELECT id FROM tasks WHERE email_id = ?", (email[0],))
        if cursor.fetchone():
            continue # Skip if already processed

        print(f"Analyzing email ID {email[0]} for tasks (Local LLM)...")
        
        prompt = f"""
        Analyze this email and identify any action items. 
        Return ONLY a JSON object: {{"task": "description", "due_date": "YYYY-MM-DD or None", "priority": "High/Medium/Low"}}.
        If no task exists, return {{"task": "None"}}.
        Email Body: {email[2][:1000]}
        """
        
        try:
            # 3. Request to local Ollama server
            response = requests.post("http://localhost:11434/api/generate", json={
                "model": "llama3",
                "prompt": prompt,
                "format": "json",
                "stream": False
            })
            
            result = response.json()
            data = json.loads(result['response'])
            
            # 4. Save if a task exists
            if data.get("task") and data.get("task") != "None":
                cursor.execute('''
                    INSERT INTO tasks (email_id, task_description, due_date, priority)
                    VALUES (?, ?, ?, ?)
                ''', (email[0], data['task'], data.get('due_date'), data.get('priority')))
                print(f"Extracted Task: {data['task']}")
        
        except Exception as e:
            print(f"Error processing email {email[0]}: {e}")
    
    conn.commit()
    conn.close()
    print("Task extraction cycle complete.")

if __name__ == "__main__":
    extract_tasks_from_db()