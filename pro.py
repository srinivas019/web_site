from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

pro = Flask(__name__)

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017')
db = client['mydatabase']
@pro.route('/')
def index():
    return render_template('signup.html')

@pro.route('/signup', methods=['POST'])
def signup():
    username = request.form['username']
    mailid = request.form['mailid']
    contact= request.form['phoneno']
    setpassword= request.form['[password]']
    password = request.form['password']

    return redirect(url_for('success'))

@pro.route('/success')
def success():
    return 'signup successful!'

if __name__ == '__main__':
    pro.run(debug=True)