from flask import Flask, request, session, redirect, url_for, flash
from flask_login import logout_user
import mysql.connector
import os
from os import getenv
from dotenv import load_dotenv
import database

app = Flask(__name__)

#Set the secret key
load_dotenv()
app.config["SECRET_KEY"] = os.getenv("secret_key")
app.config['SESSION_TYPE'] = 'filesystem'

#main route
@app.route('/')
def root():
    if 'username' in session:
        return "Logged in as %s" % escape(session['username'])
    return "You are not logged in"

#register route
@app.route('/register')
def register():
   #request User registration info
    Username = request.args.get("username")
    Password = request.args.get("password")
    Email = request.args.get("email")
    Role = request.args.get("role")

    #add user info to the table User
    add_user = "INSERT INTO User (username, password, email, role) VALUES (%s, %s, %s, %s)"
    user_info = (Username, Password, Email, Role)
    database.mycursor.execute(add_user, user_info)
    database.db.commit()
    database.db.close()

    return "Registration Complete"

#login route
@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('root'))
    return 'You are logged in'

#logout route
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('root'))

if __name__ == '__main__':
    app.debug = True
    app.run()

