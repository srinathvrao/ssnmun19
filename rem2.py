import easyimap

login = 'ssnmun.payment@gmail.com'
password = 'jerrygeorgethomas'
imapper = easyimap.connect('imap.gmail.com', login, password)
for mail_id in imapper.listids(limit=100):
    mail = imapper.mail(mail_id)
    print(mail.body)
    print("======")
