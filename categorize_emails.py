import sqlite3
import requests
import json

def categorize_all():
    db_path = r'E:\Email_Agent_Project\email_agent.db'
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Get all uncategorized emails
    cursor.execute("SELECT id, subject, body FROM emails WHERE category = 'Uncategorized'")
    emails = cursor.fetchall()
    
    for email in emails:
        print(f"Categorizing email {email[0]}...")
        prompt = f"Classify this email subject into one of these: [Professional, Education, Community, Personal]. Return only the category name. Subject: {email[1]}"
        
        try:
            response = requests.post("http://localhost:11434/api/generate", json={
                "model": "llama3",
                "prompt": prompt,
                "stream": False
            })
            category = response.json()['response'].strip()
            
            # Update the database
            cursor.execute("UPDATE emails SET category = ? WHERE id = ?", (category, email[0]))
            print(f"Set category to: {category}")
        except Exception as e:
            print(f"Error categorizing: {e}")
            
    conn.commit()
    conn.close()

if __name__ == "__main__":
    categorize_all()