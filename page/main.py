from flask import Flask, render_template, request, jsonify
import csv
from flask_pymongo import PyMongo
import datetime
from datetime import timedelta  
import os


app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://srinath:srinath@localhost:27017/myDatabase"
mongo = PyMongo(app)

@app.route("/")
def displ():
    return render_template("index.html")


@app.route("/updateDB",methods=['GET','POST'])
def update_db():
    print("HELLO WORLD")
    dic = str(request.data)
    print(dic)
    with open('data.txt','a') as file:
        file.write(str(dic))
    l = dic.split('&')
    x = {y.split('=')[0] : y.split('=')[1] for y in l}
    z = mongo.db.questions.insert_one(x)
    if z.acknowledged:
        respondic = {"data":"Submitted your question!"}
        return jsonify(respondic)
    else:
        respondic = {"data":"Error submitting your question. Please try again later."}
        return jsonify(respondic)


if __name__ == "__main__":
    app.run(host="139.59.33.113",port=8085)


