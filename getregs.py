from flask import Flask, render_template, request, jsonify
import csv
import pickle
from flask_pymongo import PyMongo
app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://srinath:srinath@localhost:27017/myDatabase"
mongo = PyMongo(app)

testh = mongo.db.questions.find()
with open('questions.data','w') as file:
    for doc in testh:
        for key,values in doc.items():
            if str(key) in [ "_id","anon"]:
                continue
            st = str(values)+"\n"
            file.write(st)
        file.write("\n\n")

