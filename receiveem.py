import easyimap

login = 'srinathv17111@it.ssn.edu.in'
password = '######'

imapper = easyimap.connect('imap.gmail.com', login, password)
for mail_id in imapper.listids(limit=1):
    mail = imapper.mail(mail_id)
    print(mail.body)

import os
os.system("python /home/srinath/Desktop/mun19/ssnmun19/receiveem.py")