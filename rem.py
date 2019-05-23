# import easyimap

# login = 'srinathv17111@it.ssn.edu.in'
# password = 'Gurukrupa23091999'
# count=0	
# while True:
# 	imapper = easyimap.connect('imap.gmail.com', login, password)
# 	for mail_id in imapper.listids(limit=1):
# 	    mail = imapper.mail(mail_id)
# 	    print(mail.body)
# 	print(count)
# 	count+=1

import smtplib
import time
import imaplib
import email

ORG_EMAIL   = "@it.ssn.edu.in"
FROM_EMAIL  = "srinathv17111" + ORG_EMAIL
FROM_PWD    = "Gurukrupa23091999"
SMTP_SERVER = "imap.gmail.com"
SMTP_PORT   = 993

# -------------------------------------------------
#
# Utility to read email from Gmail Using Python
#
# ------------------------------------------------
f=open("log2.txt","w+")
def read_email_from_gmail():
    try:
        count = 0
        while True:
        	mail = imaplib.IMAP4_SSL(SMTP_SERVER)        	
	        mail.login(FROM_EMAIL,FROM_PWD)
	        mail.select('inbox')

	        type, data = mail.search(None, 'ALL')
	        mail_ids = data[0]

	        id_list = mail_ids.split()   
	        first_email_id = int(id_list[0])
	        latest_email_id = int(id_list[-1])
	        last = latest_email_id - 1
	        for i in range(latest_email_id,last, -1):
	            typ, data = mail.fetch(i, '(RFC822)' )

	            for response_part in data:
	                if isinstance(response_part, tuple):
	                    msg = email.message_from_string(response_part[1])
	                    # for k,v in msg:
	                    email_subject = msg['Content-Type']
	                    email_from = msg['from']
	                    print 'From : ' + email_from + '\n'
	                    # print msg
	        print 'testing '+str(count)
	        f.write("testing %d\n" % count)
	        count = count + 1
    except Exception, e:
        print str(e)

read_email_from_gmail()