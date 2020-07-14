from flask import Flask, request, session, redirect, url_for, flash
from flask_login import logout_user
import mysql.connector
import os
from os import getenv
from dotenv import load_dotenv
import database
from database import mycursor
from flask_session import Session

app = Flask(__name__,
    static_folder='build',
    template_folder='build',
    static_url_path='/')

sess = Session()

#Set the secret key
load_dotenv()
#app.config["SECRET_KEY"] = os.getenv("secret_key")
#app.config['SESSION_TYPE'] = 'memcache'


#main route
@app.route('/')
def root():
    #if 'username' in session:
    #    return "Logged in as %s" % escape(session['username'])
    return app.send_static_file('index.html')

#register route
@app.route('/register')
def register():
   #request User registration info
    Username = request.args.get("username")
    Password = request.args.get("password")
    Email = request.args.get("email")
    Role = request.args.get("role")

    # if this returns a user, then the email already exists in the database
    mycursor.execute('SELECT email from User WHERE email = %(email)s', {'email' : Email })
    checkUser = mycursor.fetchall()

    # if a user is returned, the user is rerouted to the register page, where they can try a different email.
    if checkUser:
        flash('This email has already been registered.')
        return redirect(url_for('register'))

    #add user info to the table User
    add_user = "INSERT INTO User (username, password, email, role) VALUES (%s, %s, %s, %s)"
    user_info = (Username, Password, Email, Role)
    database.mycursor.execute(add_user, user_info)
    database.db.commit()
    #database.db.close()

    return "Registration Complete"

#login route
@app.route('/login', methods = ['GET', 'POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    mycursor.execute('SELECT * FROM User WHERE username = %s and password = %s', (username, password))
    account = mycursor.fetchone()
    database.db.close()

    if account:
        session['username'] = session.form('username')
        return 'Logged in successfully!'

    else:
        flash('Incorrect username/password')
        return redirect(url_for('login'))

#logout route
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('root'))

if __name__ == '__main__':
    app.secret_key = os.getenv("secret_key")
    app.debug = True

    sess.init_app(app)
    app.run()

