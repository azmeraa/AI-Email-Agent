from imap_tools import MailBox
import sqlite3

# Replace with your actual credentials
EMAIL_USER = "azmeraabebe26@gmail.com"
EMAIL_PASS = "vigt vkbq ljwx kscy"

def save_to_db(msg):
    conn = sqlite3.connect('email_agent.db')
    cursor = conn.cursor()
    # Check if this email subject already exists to avoid duplicates
    cursor.execute('SELECT id FROM emails WHERE subject = ?', (msg.subject,))
    if not cursor.fetchone():
        cursor.execute('''
            INSERT INTO emails (sender, subject, received_date, body, category)
            VALUES (?, ?, ?, ?, ?)
        ''', (msg.from_, msg.subject, str(msg.date), msg.text[:500], 'Uncategorized'))
        conn.commit()
        print(f"Saved to DB: {msg.subject}")
    else:
        print(f"Skipped (already in DB): {msg.subject}")
    conn.close()

with MailBox('imap.gmail.com').login(EMAIL_USER, EMAIL_PASS) as mailbox:
    for msg in mailbox.fetch(limit=10, reverse=True):
        save_to_db(msg)