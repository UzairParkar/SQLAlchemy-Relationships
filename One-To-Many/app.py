from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from datetime import date, UTC, datetime

#Initialises the flask App
app = Flask(__name__)

''' I have a feeling that this will be very useful to me in the future
so i have decided to document this a little with comments'''

#To configure a SQLite Database=
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///test.db"

#to Configure a MySQL Database
"app.config(['SQLALCHEMY_DATABASE_URI']) = 'mysql://root:root@localhost/Test'"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#Sqlalchemy Maps the data
db = SQLAlchemy(app)

#Marshmallow Helps in Serializing and Desirealizing the Data
ma = Marshmallow(app) # this has no use in this mapping repository

class User(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(30),nullable = False)
    email = db.Column(db.String(30))
    password =  db.Column(db.String(9),nullable = False)
    Profiles = db.relationship('Profile',backref = 'profile',lazy = True)

    def __repr__(self) -> str :
        return f'<User:{self.username}>'


class Profile(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(35),nullable = False)
    dob = db.Column(db.String(10),nullable = True)
    acc_created = db.Column(db.DateTime,default = datetime.utcnow)
    bio = db.Column(db.String(40),nullable = True)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id',ondelete='CASCADE'),unique = True)

    def __repr__(self) -> str:
        return f'<Profile:{self.name}'
        

#Queries
'''To create a database'''

with app.app_context():
    db.create_all()




        
#Runs the App
if __name__ == '__main__':
    app.run(debug=True)