from flask import Flask, render_template, session, redirect
from functools import wraps


app = Flask(__name__)
app.secret_key = b'\xcc^\x91\xea\x17-\xd0W\x03\xa7\xf8J0\xac8\xc5'



# Decorators
def login_required(f):
  @wraps(f)
  def wrap(*args, **kwargs):
    if 'logged_in' in session:
      return f(*args, **kwargs)
    else:
      return redirect('/')
  
  return wrap

# Routes

from models import User
@app.route('/')
def hello_world():
  return render_template("home.html")
@app.route('/dashboard/')
def dashboard():
  return render_template('dashboard.html')

@app.route('/user/signup', methods=['POST'])
def signup1():
  return User().signup()

@app.route('/user/signout')
def signout1():
  return User().signout()

@app.route('/user/login', methods=['POST'])
def login1():
  return User().login() 

if __name__ == "__main__":
    app.run(debug=True,port=5000)

