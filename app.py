from datetime import timedelta

from flask import Flask, render_template, request, redirect, session, url_for
from pymongo import MongoClient
import secrets

secret_key = secrets.token_hex(16)
print(secret_key)


app = Flask(__name__)
app.secret_key = secret_key
app.permanent_session_lifetime = timedelta(minutes=10)
client = MongoClient('mongodb://localhost:27017/')
db = client['chatbot']  # Replace 'mydatabase' with your database name
users_collection = db['users']  # Collection for storing user information


def login_required(route_function):
    def wrapper(*args, **kwargs):
        if 'username' not in session:
            return redirect('/login')
        return route_function(*args, **kwargs)
    return wrapper



@app.route('/')
@login_required
def index():
    return f"Hello, {session['username']}! You are already logged in."
    # if 'username' in session:
    #     return f"Hello, {session['username']}! You are already logged in."
    # return redirect('/login')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = users_collection.find_one({'username': username, 'password': password})
        if user:
            session['username'] = username
            return redirect('/dashboard')
        else:
            error = 'Invalid username or password'
            # return redirect(url_for('login', error=error))
            return render_template('login-register.html', error='Invalid username or password')
    # error = request.args.get('error')
    return render_template('login-register.html')


@app.route('/signup', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']

        existing_user = users_collection.find_one({'username': username})
        if existing_user:
            return render_template('login-register.html', error='Username already exists')

        existing_email = users_collection.find_one({'email': email})
        if existing_email:
            return render_template('login-register.html', error='email already exists')

        user = {'username': username, 'password': password, 'email': email}
        users_collection.insert_one(user)
        session['username'] = username
        return redirect('/config')

    return render_template('login-register.html')

@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        return render_template('bot.html')
    return redirect('/login')

# @app.route('/config')
# def config():
#     if 'username' in session:
#         return render_template('config-form.html')
#     return redirect('/login')

@app.route('/config', methods=['GET', 'POST'])
def config():
    if 'username' not in session:
        return redirect('/login')

    if request.method == 'POST':
        username = session['username']
        url = request.form['url']
        access_token = request.form['accesstoken']
        project_id = request.form['projectid']

        # Update the user document with the configuration values
        users_collection.update_one({'username': username}, {'$set': {'url': url, 'access_token': access_token, 'project_id': project_id}})

        return redirect('/dashboard')

    return render_template('config-form.html')


@app.route('/logout')
def logout():
    session.pop('username', None)
    session.clear()
    return redirect('/login')


if __name__ == '__main__':
    app.run()



























# from flask import Flask, render_template, session, redirect
# from functools import wraps
# import pymongo
#
# app = Flask(__name__)
# # app.secret_key = b'\xcc^\x91\xea\x17-\xd0W\x03\xa7\xf8J0\xac8\xc5'
#
# # Database
# client = pymongo.MongoClient('localhost', 27017)
# db = client.chatbot
#
# # Decorators
# def login_required(f):
#   @wraps(f)
#   def wrap(*args, **kwargs):
#     if 'logged_in' in session:
#       return f(*args, **kwargs)
#     else:
#       return redirect('/')
#
#   return wrap
#
# # Routes
# from user import routes
#
# @app.route('/')
# def home():
#   return render_template('login-register.html')
#
# # @app.route('/dashboard/')
# # @login_required
# # def dashboard():
# #   return render_template('dashboard.html')
# #
# if __name__ == '__main__':
#     app.run()
