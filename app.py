from flask import Flask, render_template, session, redirect
from functools import wraps
import pymongo

app = Flask(__name__)
app.secret_key = b'\x8f^\x8as\xca]\xf6\\Z\x86\x19Cl\x07\x1f\x97'

## Database
client = pymongo.MongoClient('localhost', 27017)
db = client.user_login_system


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
from user import routes
from api import routes


@app.route('/')
@app.route('/index/')
def index():
    phone = 's9+'
	return render_template('index.html', phone=phone)


@app.route('/dashboard/')
@login_required
def dashboard():
    return render_template('dashboard.html')

