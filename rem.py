# import easyimap

# login = 'srinathv17111@it.ssn.edu.in'
# password = '#######'
# count=0	
# while True:
# 	imapper = easyimap.connect('imap.gmail.com', login, password)
# 	for mail_id in imapper.listids(limit=1):
# 	    mail = imapper.mail(mail_id)
# 	    print(mail.body)
# 	print(count)
# 	count+=1

#import smtplib
import time
import imaplib
import email
import sys
import os

ORG_EMAIL   = "@gmail.com"
FROM_EMAIL  = "ssnmun.payment" + ORG_EMAIL
FROM_PWD    = "jerrygeorgethomas"
SMTP_SERVER = "imap.gmail.com"
SMTP_PORT   = 993

# -------------------------------------------------
#
# Utility to read email from Gmail Using Python
#
# ------------------------------------------------

def read_email_from_gmail():
    try:
        #count = 0
        #while True:
        mail = imaplib.IMAP4_SSL(SMTP_SERVER)
        mail.login(FROM_EMAIL,FROM_PWD)
        mail.select('inbox')
        type, data = mail.search(None, 'ALL')
        mail_ids = data[0]

        id_list = mail_ids.split()
        first_email_id = int(id_list[0])
        latest_email_id = int(id_list[-1])
        for i in range(latest_email_id,first_email_id, -1):
            typ, data = mail.fetch(i,"")
            for response_part in data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_string(response_part[1])
                    # for k,v in msg:
                    email_subject = msg['Content-Type']
                    email_from = msg['from']
                    print(email_from)
            print("\n====================\n")
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)
read_email_from_gmail()
