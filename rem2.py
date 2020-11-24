import easyimap

login = 'ssnmun.payment@gmail.com'
password = '****'
imapper = easyimap.connect('imap.gmail.com', login, password)
for mail_id in imapper.listids(limit=100):
    mail = imapper.mail(mail_id)
    x = [str(y) for y in str(mail.body).split('\n')]
    le = len(x)
    em=""
    for i in range(7,le):
    	if x[i].strip()[:8].lower() == "<p>email":
    		st = x[i].strip()[8:].strip()
    		em = st[:len(st)-4].strip()
    		break

    print("======")
