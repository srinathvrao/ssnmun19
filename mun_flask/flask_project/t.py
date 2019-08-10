import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.encoders import encode_base64
import os

login = 'ssnmun.payment@gmail.com'
password = 'jerrygeorgethomas'
sender = 'ssnmun.payment@gmail.com'
receivers = ['srinathv1001@gmail.com']

msg = MIMEMultipart()
msg['From'] = sender
msg['To'] = ", ".join(receivers)
msg['Subject'] = "Test Message"

# Simple text message or HTML
TEXT = "Hello everyone,\n"
TEXT = TEXT + "\n"
TEXT = TEXT + "Important message.\n"
TEXT = TEXT + "\n"
TEXT = TEXT + "Thanks,\n"
TEXT = TEXT + "SMTP Robot"

msg.attach(MIMEText(TEXT))
smtpObj = smtplib.SMTP('smtp.gmail.com:587')
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login(login, password)
smtpObj.sendmail(sender, receivers, msg.as_string())
