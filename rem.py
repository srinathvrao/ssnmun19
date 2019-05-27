import smtplib
import time
import imaplib
import email

    # -------------------------------------------------
    #
    # Utility to read email from Gmail Using Python
    #
    # ------------------------------------------------

ORG_EMAIL   = "@gmail.com"
FROM_EMAIL  = "ssnmun.payment" + ORG_EMAIL
FROM_PWD    = "jerrygeorgethomas"
SMTP_SERVER = "imap.gmail.com"
SMTP_PORT   = 993

def read_email_from_gmail():
    try:
        mail = imaplib.IMAP4_SSL(SMTP_SERVER)
        mail.login(FROM_EMAIL,FROM_PWD)
        mail.select('inbox')

        type, data = mail.search(None, 'ALL')
        mail_ids = data[0]

        id_list = mail_ids.split()
        first_email_id = int(id_list[0])
        latest_email_id = int(id_list[-1])


        for i in range(latest_email_id,first_email_id, -1):
            typ, data = mail.fetch(str(i), '(RFC822)' )

        for response_part in data:
            if isinstance(response_part, tuple):
                msg = email.message_from_string(str(response_part[1]))
                print(msg)
            print("\n================\n")

    except Exception as e:
        raise

print(read_email_from_gmail())