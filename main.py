from flask import Flask, request
from forms import RegistrationForm, LoginForm
import mysql.connector

app = Flask(__name__)
app.config['SECRET KEY'] = '009d6ca23ae690fec6bada88ac46f0b4'

@app.route('/')
def root():
	return "<h1>Hello World!</h1>"

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)
#@app.route('/register', method = ['POST'])
#def register():
#    Username = request.args.get('username');
#    Password = request.args.get('password');
#    Email = request.args.get('email');
#    Role = request.args.get('role');
#    insert_query = "INSERT INTO User (username, password, email, role) VALUES (%s, %s, %s, %s)"
#    insert_values = (Username, Password, Email, Role);

    mycursor.execute(insert_query, insert_values);
    db.commit()


# start the flask app
if __name__ == '__main__':
	app.run()
