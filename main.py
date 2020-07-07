from flask import Flask, request
import mysql.connector
import os
from os import getenv
from dotenv import load_dotenv, find_dotenv
#print(getenv("DB_PASSWORD"))

app = Flask(__name__)

@app.route('/')
def root():
    return "Hello World"

if __name__ == '__main__':
    app.run()

#calling the load_dotenv file
load_dotenv(find_dotenv())
password = os.getenv("password_db")

#connect to server
db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "babybump",
    database = "babybump"
)

mycursor = db.cursor()

# create database and tables if they don't already exist
mycursor.execute("CREATE DATABASE IF NOT EXISTS babybump DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;".format("babybump"));
mycursor.execute("CREATE TABLE IF NOT EXISTS User (username VARCHAR(25), password VARCHAR(25), email VARCHAR(25), role VARCHAR(25), id int PRIMARY KEY AUTO_INCREMENT)")

#add user info to the table User
Username = request.args.get("username")
Password = request.args.get("password")
Email = request.args.get("email")
Role = request.args.get("role")

add_user = "INSERT INTO User (username, password, email, role) VALUES (%s, %s, %s, %s)"
user_info = (Username, Password, Email, Role)
mycursor.execute(add_user, user_info)
db.commit()

db.close()
