from flask import Flask, render_template, request
import csv
from flask_pymongo import PyMongo
import datetime
from datetime import timedelta  
import time
import easyimap
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.encoders import encode_base64
import os


app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://srinath:srinath@localhost:27017/myDatabase"
mongo = PyMongo(app)

def sendDeletedEM(em):
    try:
        login = 'ssnmun@gmail.com'
        password = 'jerrygeorgethomas'
        sender = 'ssnmun@gmail.com'
        receivers = [em]

        msg = MIMEMultipart()
        msg['From'] = sender
        msg['To'] = ", ".join(receivers)
        msg['Subject'] = "Priority Registration"

        # Simple text message or HTML
        TEXT = "Hello.\n"
        TEXT = TEXT + "\n"
        TEXT = TEXT + "Your priority registration for SSNMUN'19 exceeded the time limit and has been deleted.\n\n"

        msg.attach(MIMEText(TEXT))

        smtpObj = smtplib.SMTP('smtp.gmail.com:587')
        smtpObj.ehlo()
        smtpObj.starttls()
        smtpObj.login(login, password)
        smtpObj.sendmail(sender, receivers, msg.as_string())
        
    except Exception as e:
        print(str(e))

def sendAcceptedEM(reg,pref,em):
    try:
        login = 'ssnmun@gmail.com'
        password = 'jerrygeorgethomas'
        sender = 'ssnmun@gmail.com'
        receivers = [em]

        msg = MIMEMultipart()
        msg['From'] = sender
        msg['To'] = ", ".join(receivers)
        msg['Subject'] = "Priority Registration Confirmation"

        # Simple text message or HTML
        TEXT = "Hurrah!\n"
        TEXT = TEXT + "\n"
        TEXT = TEXT + "Your priority registration for SSNMUN'19 has been confirmed.\n\n"
        TEXT = TEXT + "Registration number: "+reg+"\n"
        TEXT = TEXT + "Preference: "+pref+"\n"
        TEXT = TEXT + "See you there!"

        msg.attach(MIMEText(TEXT))

        smtpObj = smtplib.SMTP('smtp.gmail.com:587')
        smtpObj.ehlo()
        smtpObj.starttls()
        smtpObj.login(login, password)
        smtpObj.sendmail(sender, receivers, msg.as_string())
        
    except Exception as e:
        print(str(e))

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
                                    try:
                                        sendAcceptedEM(reg,pref,em)
                                    except Exception as e:
                                        print("Error! "+str(e))

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
              #  print(s1+" "+s2+" "+str(doc["email"]))
                print(str(minutes)+" " + str(doc["email"]))
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
                    print("Deleted "+str(doc["email"]))
                    try:
                        sendDeletedEM(doc["email"])
                    except Exception as e:
                        print("Error! "+str(e))
    except Exception as e:
        print(str(e))                            
                        #t = mongo.db.regs.deleteOne({"email":em})
    time.sleep(2)
# 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
