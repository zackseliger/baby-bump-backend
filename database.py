import mysql.connector
from os import getenv
from dotenv import load_dotenv
load_dotenv()

print(getenv("DB_PASSWORD"))

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = getenv("DB_PASSWORD")
)

mycursor = db.cursor()

# create database and tables if they don't already exist
mycursor.execute("CREATE DATABASE IF NOT EXISTS {} DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;".format("babybump"))
