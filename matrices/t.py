from flask import Flask, render_template, request, jsonify
import csv
from flask_pymongo import PyMongo
app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://srinath:srinath@localhost:27017/myDatabase"
mongo = PyMongo(app)
comms = ["ECOFIN","HRC","SC"]
for comm in comms:
	with open(comm+".csv") as csv_file:
		csv_reader = csv.reader(csv_file,delimiter=',')
		for row in csv_reader:
			mongo.db.matrix.insert_one({comm:str(row[0])+"_ava"})