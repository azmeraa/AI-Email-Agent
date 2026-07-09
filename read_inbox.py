from imap_tools import MailBox

# Replace with your actual email
EMAIL_USER = "azmeraabebe26@gmail.com" 
# Paste your new 16-character App Password here, with NO spaces
EMAIL_PASS = "vigt vkbq ljwx kscy" 

try:
    # Connect to Gmail
    with MailBox('imap.gmail.com').login(EMAIL_USER, EMAIL_PASS) as mailbox:
        print("Successfully connected to Gmail!")
        
        # Fetch the 5 most recent emails
        # reverse=True ensures you get the newest ones first
        for msg in mailbox.fetch(limit=5, reverse=True):
            print(f"\n--- New Email ---")
            print(f"From: {msg.from_}")
            print(f"Subject: {msg.subject}")
            print(f"Date: {msg.date}")
            # .text provides the plain text version of the email body
            print(f"Body snippet: {msg.text[:100]}...") 
            
except Exception as e:
    print(f"An error occurred: {e}")