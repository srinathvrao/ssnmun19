import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.encoders import encode_base64
import os

login = 'emailID' # enter your email ID here
password = 'password' # enter your password here
receivers = ['ssnmun@gmail.com']

msg = MIMEMultipart()
msg['From'] = login
msg['To'] = ", ".join(receivers)
msg['Subject'] = "Payment Receipt - Priority Registration"

# Simple text message or HTML
TEXT = "Payment ID : abcde "+"\n" # Replace with payment ID.
TEXT = TEXT + "\n"

msg.attach(MIMEText(TEXT))

# filenames = ["test.txt", "test.jpg"]
# for file in filenames:
#     part = MIMEBase('application', 'octet-stream')
#     part.set_payload(open(file, 'rb').read())
#     encode_base64(part)
#     part.add_header('Content-Disposition', 'attachment; filename="%s"'
#                     % os.path.basename(file))
#     msg.attach(part)

smtpObj = smtplib.SMTP('smtp.gmail.com:587')
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login(login, password)
smtpObj.sendmail(login, receivers, msg.as_string())