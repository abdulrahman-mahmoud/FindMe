import smtplib
from email.mime.text import MIMEText

def send_match_notifcation_email(reciver):
    sender = 'Find.it.zc@gmail.com'
    password = 'vnguomfjipownzkp' 
    reciver = f'{reciver}@zewailcity.edu.eg'
    subject = 'Notofication from Find.it.zc'
    body = 'This message is send by python code script , plz dont reply thx '
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = reciver

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
        smtp_server.login(sender, password)
        smtp_server.sendmail(sender, reciver, msg.as_string())
        print("Message sent!")
send_match_notifcation_email('')