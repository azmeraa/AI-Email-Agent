from imap_tools import MailBox
import sqlite3

EMAIL_USER = "azmeraabebe26@gmail.com"
EMAIL_PASS = "vigt vkbq ljwx kscy"

def save_to_db(msg):
    conn = sqlite3.connect('email_agent.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO emails (sender, subject, received_date, body, category)
        VALUES (?, ?, ?, ?, ?)
    ''', (msg.from_, msg.subject, str(msg.date), msg.text[:500], 'Uncategorized'))
    conn.commit()
    conn.close()

with MailBox('imap.gmail.com').login(EMAIL_USER, EMAIL_PASS) as mailbox:
    for msg in mailbox.fetch(limit=5, reverse=True):
        save_to_db(msg)
        print(f"Saved: {msg.subject}")