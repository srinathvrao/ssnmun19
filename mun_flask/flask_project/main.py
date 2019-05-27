from flask import Flask, render_template, request, jsonify
import csv
from flask_pymongo import PyMongo
import datetime
from datetime import timedelta  

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://srinath:srinath@localhost:27017/myDatabase"
mongo = PyMongo(app)
@app.route("/")
def home():
	return render_template("index.html")

@app.route("/api_countries",methods=['POST'])
def fillCountries():
    try:
        testh = mongo.db.matrix.find()
        myDICK = {}
        for doc in testh:
            myDICK1 = dict(doc)
            for k,v in myDICK1.items():
                if k in myDICK.keys() and str(k) != "_id":
                    myDICK[str(k)] += "," + str(v)
                elif k not in myDICK.keys() and str(k) != "_id":
                    myDICK[str(k)] = str(v)
        for v in myDICK.values():
            print(str(v))
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
    pref = request.form["countryPref1"]
    pre = pref.split("_")
    comPref = pre[0]
    countryPref = pre[1]
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
            for doc in testh:
                lastreg = doc
            if lastreg != "":
                last = lastreg[len(lastreg)-3:]
                regID = int(last)
            reg=""
            testh = mongo.db.conregs.distinct("regno")
            lastreg=""
            for doc in testh:
                lastreg = doc
            if lastreg != "":
                last = lastreg[len(lastreg)-3:]
                regID2 = int(last)
            reg2=""
            if regID < regID2:
                regID = regID2
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
                        return "<div><p align='center'><hr /><h2>Your registration number is :  "+reg+"</h2><h3><br>Your Email-ID is : "+email+"<br>This is valid for 10 minutes, till <h2>"+str(ti) +"</h2>.<br>Enter the same E-mail ID and Registration number in the payment portal<br></h3><a href=\"http://www.ssn.edu.in/apps/mun-payment-form/\">Proceed to make payment</a><hr /></p></div>"
                    else:
                        return "<h3>Error registering in database.</h3>"

if __name__ == "__main__":
    app.run(port=8000)

