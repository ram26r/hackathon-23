import re
from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)

# Connect to the MongoDB database
client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']  # Replace 'mydatabase' with your database name
users_collection = db['users']  # Replace 'users' with your collection name


@app.route('/login', methods=['POST'])
def login():
    username = request.json['username']
    password = request.json['password']

    # Perform database query to retrieve user data
    user = users_collection.find_one({'username': username, 'password': password})

    if user:
        return jsonify({'message': 'Login successful'})
    else:
        return jsonify({'message': 'Invalid credentials'})


@app.route('/signup', methods=['POST'])
def signup():
    username = request.json['username']
    password = request.json['password']
    email = request.json['email']

    # Check if the username already exists
    if users_collection.find_one({'username': username}):
        return jsonify({'message': 'Username already exists'})

    # Validate email address using regular expression
    if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
        return jsonify({'message': 'Invalid email address'})

    # Insert Bot-Module user data into the database
    user_id = users_collection.insert_one({'username': username, 'password': password, 'email': email}).inserted_id

    return jsonify({'message': 'User created', 'user_id': str(user_id)})


if __name__ == '__main__':
    app.run()


# Insert Sample User Data:
# users_collection.insert_one({'username': 'john', 'password': 'password123'})



