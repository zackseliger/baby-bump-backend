from main import app
import os
from os import getenv
from dotenv import load_dotenv


load_dotenv()

if __name__ == '__main__':
    app.secret_key = os.getenv("secret_key")

    app.run()
