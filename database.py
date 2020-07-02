import mysql.connector
from os import getenv
from dotenv import load_dotenv
load_dotenv()

print(getenv("DB_PASSWORD"))

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd= getenv("DB_PASSWORD"),
    database = "biglistgames"
)

mycursor = db.cursor()
