from flask import Flask
app = Flask(__name__)

@app.route('/handle_data', methods=['POST'])
def handle_data():
    projectpath = request.form['name']
    # your code
    # return a response

if __name__ == "__main__":
	app.run()