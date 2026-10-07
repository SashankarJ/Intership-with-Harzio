import smtplib
from email.mime.text import MIMEText
from xmlrpc import server


THRESHOLD_CPU = 85
THRESHOLD_RAM = 90




def send_alert(message):
    msg = MIMEText(message)
    msg['Subject'] = 'System Alert'
    msg['From'] = 'monitor@example.com'
    msg['To'] = 'admin@example.com'

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('your_email@gmail.com', 'your_password')
    server.send_message(msg)
    server.quit()