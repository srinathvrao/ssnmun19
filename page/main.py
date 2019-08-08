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
    dic = request.data
    l = dic.split('&')
    m = l[0].split('=')
    n = l[1].split('=')
    question = m[1]
    topic = n[1]
    print(question) 
    print(topic)
    questiondict = {'question':question,'topic':topic}
    x = mongo.db.questions.insert_one(questiondict)
    if x.acknowledged:
        respondic = {"data":"Submitted your question!"}
        return jsonify(respondic)
    else:
        respondic = {"data":"Error submitting your question. Please try again later."}
        return jsonify(respondic)


if __name__ == "__main__":
    app.run(port=8000)


