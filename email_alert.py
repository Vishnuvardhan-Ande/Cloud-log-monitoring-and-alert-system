'''
import smtplib
from email.mime.text import MIMEText

def send_alert(message):

    sender = "your_email@gmail.com"
    receiver = "your_email@gmail.com"

    msg = MIMEText(message)
    msg["Subject"] = "Log Monitoring Alert"
    msg["From"] = sender
    msg["To"] = receiver

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender, "your_app_password")

    server.send_message(msg)
    server.quit()
'''
import mailtrap as mt

TOKEN = "78bc2c59929a7a9eb30d47312485de21"

def send_alert(message):

    mail = mt.Mail(
        sender=mt.Address(email="hello@demomailtrap.co", name="Log Monitoring System"),
        to=[mt.Address(email="vishnuande2006@gmail.com")],
        subject="Log Monitoring Alert",
        text=message,
        category="Log Alert"
    )

    client = mt.MailtrapClient(token=TOKEN)
    response = client.send(mail)

    return response
