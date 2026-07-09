import sqlite3
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(api_key="vigt vkbq ljwx kscy")

def get_ai_category(text):
    # This prompt tells the AI how to behave
    prompt = f"Classify this email into one of these categories: [Technical, Job/Academic, News, Personal, Security]. Return ONLY the category name. Text: {text[:500]}"
    
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

def process_and_classify():
    conn = sqlite3.connect('email_agent.db')
    cursor = conn.cursor()
    
    # Select only uncategorized emails
    cursor.execute("SELECT id, body FROM emails WHERE is_processed = 0")
    emails = cursor.fetchall()
    
    for email in emails:
        print(f"Classifying ID {email[0]}...")
        category = get_ai_category(email[1])
        
        cursor.execute('''
            UPDATE emails 
            SET category = ?, is_processed = 1 
            WHERE id = ?
        ''', (category, email[0]))
        print(f"Result: {category}")
        
    conn.commit()
    conn.close()

if __name__ == "__main__":
    process_and_classify()