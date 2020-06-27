from flask import Flask
app = Flask(__name__)

@app.route('/')
def root():
	return "<h1>Hello World!</h1>"


# start the flask app
if __name__ == '__main__':
	app.run()