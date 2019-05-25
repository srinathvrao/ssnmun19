from flask import Flask, render_template, request
import csv

app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")

@app.route('/handle_data', methods=['POST'])
def handle_data():
    name = request.form['name']
    email = request.form["email"]
    country = request.form["country"]
    with open('prio_registered.csv') as csv_file:
    	csv_reader = csv.reader(csv_file, delimiter=',')
    	line_count = 0
    	for row in csv_reader:
    		if row[1] == email:
    			return "<h3>E-Mail already used for registration.<h3>"
    return name+" "+email+" "+country
    # your code
    # return a response

if __name__ == "__main__":
    app.run(port=8000)
