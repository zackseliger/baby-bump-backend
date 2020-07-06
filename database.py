import mysql.connector
from os import getenv
from dotenv import load_dotenv
#load_dotenv()
#print(getenv("DB_PASSWORD"))

#connect to server
db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = ,
    database = "babybump"
)

mycursor = db.cursor()

# create database and tables if they don't already exist
mycursor.execute("CREATE DATABASE IF NOT EXISTS babybump DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;".format("babybump"));
mycursor.execute("CREATE TABLE IF NOT EXISTS User (username VARCHAR(25), password VARCHAR(25), email VARCHAR(25), role VARCHAR(25), id int PRIMARY KEY AUTO_INCREMENT)")

#adding users to the User table - the method of getting the Username, Password, Email, and Role need to be changed
#- just have it this way to show that info being passed from front to back end
add_user = "INSERT INTO User (username, password, email, role) VALUES (%s, %s, %s, %s)"
Username = input('Username: ')
Password = input('Password: ')
Email = input('Email: ')
Role = input('Role: ')
user_info = (Username, Password, Email, Role)
mycursor.execute(add_user, user_info)
db.commit()

db.close()
