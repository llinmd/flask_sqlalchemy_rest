from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# Init app
app = Flask(__name__)

# Load Config file:
app.config.from_object("config.DevelopmentConfig")

# Init db
db = SQLAlchemy(app)
# Init ma
ma = Marshmallow(app)

# User Class/Model
class User(db.Model):
    __tablename__ = 'auth_credentials'

    firstname = db.Column(db.String(20), nullable=False)
    lastname = db.Column(db.String(20), nullable=False)
    username = db.Column(db.String(20), primary_key=True)
    password = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(25), nullable=False, unique=True)

    def __init__(self, firstname, lastname, username, password, email):
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.password = password
        self.email = email

    def __repr__(self):
        return f"{self.firstname} {self.lastname} {self.username} {self.email}"

# User Schema
class UserSchema(ma.Schema):
    class Meta:
        # fields to expose
        fields = ('firstname', 'lastname', 'username', 'password', 'email')

# Init schema
user_schema = UserSchema()
users_schema = UserSchema(many=True)

# Create a user
@app.route('/user', methods=['POST'])
def add_user():
    user = User.query.get(request.json['username'])
    if user is None:
        firstname = request.json['firstname']
        lastname = request.json['lastname']
        username = request.json['username']
        password = request.json['password']
        email = request.json['email']
        user = User(firstname, lastname, username, password, email)
        db.session.add(user)
        db.session.commit()
    else:
        raise Exception('User already exists')

    return user_schema.jsonify(user)

# Get all users
@app.route('/user', methods=['GET']) 
def get_users():
    all_users = User.query.all()
    result = users_schema.dump(all_users)
    return jsonify(result)

# Get a user
@app.route('/user/<username>', methods=['GET']) 
def get_user(username):
    user = User.query.get_or_404(username)
    return user_schema.jsonify(user)

# Update a user
@app.route('/user/<username>', methods=['PUT'])
def update_user(username):
    user = User.query.get_or_404(username)

    user.firstname = request.json['firstname']
    user.lastname = request.json['lastname']
    user.password = request.json['password']
    user.email = request.json['email']
    db.session.commit()

    return user_schema.jsonify(user)

# Delete a user
@app.route('/user/<username>', methods=['DELETE']) 
def delete_user(username):
    user = User.query.get_or_404(username)
    db.session.delete(user)
    db.session.commit()

    return user_schema.jsonify(user)
 
# Run Server
if __name__ == '__main__':
    app.run(debug=True)
