import smtplib
from email.mime.text import MIMEText

import os
from dotenv import load_dotenv

# Load variables from .env file
# -------------------------
def send_match_notification_email(reciver):
    load_dotenv()
    sender = os.getenv("EMAIL_SENDER", "")
    password = os.getenv("EMAIL_PASSWORD", "")
    subject = 'Notification from Find.it.zc'
    body = 'This message is send by python code script , plz dont reply thx '
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = reciver

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
        smtp_server.login(sender, password)
        smtp_server.sendmail(sender, reciver, msg.as_string())
        print("Message sent!")
send_match_notification_email('')