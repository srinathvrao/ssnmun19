from flask import Flask, render_template, request
import csv
from flask_pymongo import PyMongo
import datetime
from datetime import timedelta  
import time
import easyimap
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://srinath:srinath@localhost:27017/myDatabase"
mongo = PyMongo(app)

while True:
    try:
        testh = mongo.db.regs.count_documents({})
        if testh>0:
            # read e-mails.
            emails=[]
            test = mongo.db.regs.distinct("email")
            for email in test:
                emails.append(email)
            login = 'ssnmun.payment@gmail.com'
            password = 'jerrygeorgethomas'
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
                        
                if em != "":
                    for em1 in emails:
                        if em==em1:
                            print(em+".... found boiii")
                            #em has done the payment.
                            # move him from regs to conregs
                            fr = mongo.db.regs.find({"email":em})
                            for f in fr:
                                myDICK = { 
                                    "regno":f["regno"],
                                    "email":f["email"],
                                    "college":f["college"],
                                    "phone":f["phone"],
                                    "nomuns":f["nomuns"],
                                    "munexp":f["munexp"],
                                    "pref":f["pref"],
                                    "time":str(datetime.datetime.now().time())
                                }
                                x = mongo.db.conregs.insert_one(myDICK)
                                if x.acknowledged:
                                    pref=f["pref"]
                                    reg = f["regno"]
                                    c=0
                                    le = len(pref)
                                    for i in range(le):
                                        if pref[i]=="_":
                                            c=i
                                            break
                                    # pref[:c] - committee
                                    # pref[c+1:] - country
                                    myquery = { pref[:c]:  pref[c+1:]+ "_pri" }
                                    newvalues = { "$set": { pref[:c]: pref[c+1:]+"_loc" } }
                                    mongo.db.matrix.update_one(myquery,newvalues)
                                    mongo.db.regs.delete_one({"email":em})
                                    # send person a confirmation email.
                                    message = Mail(
                                           from_email='ssnmun@gmail.com',
                                           to_emails=email,
                                           subject='Priority Registration Confirmation',
                                           html_content="Hurrah! Your priority registration for the MUN has been confirmed.<br>Registration number - "+reg+"<br>Preference: "+pref+"<br>See you there!~")
                                    try:
                                        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
                                        response = sg.send(message)
                                        print("SENT CONFIRMATION!!")

                                    except Exception as e:
                                        print("Error! "+str(e.message))

            testh = mongo.db.regs.find()
            for doc in testh:
                regtime = doc["time"]
                no = str(datetime.datetime.now().time())
                # no and regtime
                s1 = regtime[:8]
                s2 = no[:8]
                FMT = '%H:%M:%S'
                tdelta = datetime.datetime.strptime(s2, FMT) - datetime.datetime.strptime(s1, FMT)
                if tdelta.days < 0:
                    tdelta = timedelta(days=0,seconds=tdelta.seconds, microseconds=tdelta.microseconds)
                seconds = tdelta.total_seconds()
                hours = seconds // 3600
                minutes = (seconds % 3600) // 60
                seconds = seconds % 60
                print(s1+" "+s2+" "+str(doc["email"]))
                print(str(minutes))
                if minutes >= 10:
                    # doc["email"]
                    pref = doc["pref"]
                    c=0
                    le = len(pref)
                    for i in range(le):
                        if pref[i]=="_":
                            c=i
                            break
                    mongo.db.regs.delete_one({"email":doc["email"]})
                    myquery = { pref[:c]:  pref[c+1:]+ "_pri" }
                    newvalues = { "$set": { pref[:c]: pref[c+1:]+"_ava" } }
                    mongo.db.matrix.update_one(myquery,newvalues)
                    message = Mail(
                               from_email='ssnmun@gmail.com',
                               to_emails=email,
                               subject='Priority Registration Deleted',
                               html_content='Sorry! Your priority registration for the MUN has exceeded the time limit, and has been deleted.')
                    try:
                        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
                        response = sg.send(message)
                    except Exception as e:
                        print("Error! "+str(e.message))
    except Exception as e:
        print(str(e))                            
                        #t = mongo.db.regs.deleteOne({"email":em})
    time.sleep(2)
# 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