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
app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://srinath:srinath@localhost:27017/myDatabase"
mongo = PyMongo(app)

co = "United Kingdom of Great Britain and Northern Ireland_ava"
myquery = { "DISEC": co}
newvalues = { "$set": { "DISEC": co+"_loc" } }

mongo.db.matrix.update_one(myquery,newvalues)

if x.acknowledged:
    print("done")
