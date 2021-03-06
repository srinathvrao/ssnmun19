from flask import Flask, render_template, request, jsonify
import csv
from flask_pymongo import PyMongo
import datetime
from datetime import timedelta  

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.encoders import encode_base64
import os

def sendFirstem(reg,pref,em,ti):
    try:
        login = 'ssnmun@gmail.com'
        password = 'jerrygeorgethomas'
        sender = 'ssnmun@gmail.com'
        receivers = [em]

        msg = MIMEMultipart()
        msg['From'] = sender
        msg['To'] = ", ".join(receivers)
        msg['Subject'] = "SSNMUN'19 Priority Registration"
        # Simple text message or HTML
        TEXT = "Registration number: "+reg+"\n"
        TEXT = TEXT + "Preference: "+pref+"\n"
        TEXT = TEXT + "This is valid for 10 minutes, till "+str(ti) +".\n"
        TEXT = TEXT + "Enter the same E-mail ID and Registration number in the payment portal - \nhttp://www.ssn.edu.in/apps/mun-payment-form/"

        msg.attach(MIMEText(TEXT))

        smtpObj = smtplib.SMTP('smtp.gmail.com:587')
        smtpObj.ehlo()
        smtpObj.starttls()
        smtpObj.login(login, password)
        smtpObj.sendmail(sender, receivers, msg.as_string())
        
    except Exception as e:
        print(str(e))

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://srinath:srinath@localhost:27017/myDatabase"
mongo = PyMongo(app)
@app.route("/")
def displ():
    return render_template("index.html")
# @app.route("/testinghereboiz")
# def home():
# 	return render_template("index.html")

@app.route("/api_countries",methods=['POST'])
def fillCountries():
    try:
        s = request.get_data()
        s = str(s)
        x = s[2:(len(s)-1)]
        s = x
        testh = mongo.db.matrix.distinct(s)
        myDICK = {}
        count=0

        for doc in testh:

            s = str(doc).split("_")
            if s[1] == "ava":
                myDICK[str(count)] = s[0]
                count+=1
        #print(myDICK)
        return jsonify(myDICK)
    except Exception as e:
        print(str(e))
        return "",500

@app.route('/handle_data', methods=['POST'])
def handle_data():
    name = request.form['name']
    college = request.form['college']
    phone = request.form['phone_no']
    email = request.form['email']
    nomuns = request.form['no_del']
    exp = request.form["exp"]
    comPref = request.form["comPref1"]
    countryPref = request.form["countryPref1"]
    # pref = request.form["countryPref1"]
    pref = comPref+"_"+countryPref
#    print(pref)
    # comPref = pre[0]
    # countryPref = pre[1]
    testh = mongo.db.regs.find({"email": email})
    check=0
    for doc in testh:
    	print(doc)
    	check=1
    if check==1:
        return "<h3>E-mail already used for another registration.</h3>"
    else:
        testh = mongo.db.conregs.find({"email": email})
        check=0
        for doc in testh:
            check=1
            break
        if check==1:
            return "<h3>E-mail already used for another registration.</h3>"
        else:
            testh = mongo.db.regs.distinct("regno")
            lastreg=""
            regID = 0
            regID2 = 0
            regsno=[]
            for doc in testh:
                lastreg = doc[len(doc)-3:]
                regsno.append(int(lastreg))
            if lastreg != "":
                last = lastreg[len(lastreg)-3:]
                regID = int(last)
            reg=""
            testh = mongo.db.conregs.distinct("regno")
            lastreg=""
            for doc in testh:
                lastreg = doc[len(doc)-3:]
                regsno.append(int(lastreg))
            # print(regsno)
            # print(max(regsno))
            regID = max(regsno)
            regID+=1
            if regID < 10:
                reg = "P"+comPref+"00"+str(regID)
            elif regID < 100:
                reg = "P"+comPref+"0"+str(regID)
            else:
                reg = "P"+comPref+str(regID)

            # check if pref was taken in regs
            testh = mongo.db.regs.find({"pref":pref})
            check=0
            for doc in testh:
                check=1
                break
            if check==1:
                return "<h3>"+comPref +" - "+countryPref +" has already been registered for. <br>Too late! :(</h3>"
            else:
                # check if pref was taken in conregs.
                testh = mongo.db.conregs.find({"pref":pref})
                check=0
                for doc in testh:
                    print(doc)
                    check=1
                    break
                if check==1:
                    return "<h3>"+comPref +" - "+countryPref +" has already been taken. <br>Too late! :(</h3>"
                else:
                    myDICK = { "regno":reg,"email": email, "name": name,"college":college, "phone":phone,"nomuns":nomuns,"munexp":exp,"pref":pref,"time": str(datetime.datetime.now().time())}
                    x = mongo.db.regs.insert_one(myDICK)
                    
                    myquery = { comPref: countryPref+"_ava" }
                    newvalues = { "$set": { comPref: countryPref+"_pri" } }

                    mongo.db.matrix.update_one(myquery,newvalues)

                    if x.acknowledged:
                        ti = datetime.datetime.now() + timedelta(seconds=600) 
                        try:
                            sendFirstem(reg,pref,email,ti)
                            return "<div><p align='center'><hr /><h2>Your registration number is :  "+reg+"</h2><h3><br>Your Email-ID is : "+email+"<br>This is valid for 10 minutes, till <h2>"+str(ti) +"</h2>.<br>Enter the same E-mail ID and Registration number in the payment portal<br></h3><a href=\"http://www.ssn.edu.in/apps/mun-payment-form/\">Proceed to make payment</a><hr /> <h5>Check E-mail inbox/spam for details.</h5></p></div>"
                        except Exception as e:
                            print("Error!! ======= "+str(e))
                            return "Error!!"
                        
                    else:
                        return "<h3>Error registering in database.</h3>"

if __name__ == '__main__':
    app.run(port=8000)

