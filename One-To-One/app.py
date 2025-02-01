from flask import Flask, request,jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(20))
    profile = db.relationship('Profile',backref = 'user',uselist = False)

    def __repr__(self):
        return f"<User:{self.name}>"
    
class Profile(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(20))
    user_id = db.Column(db.Integer,db.ForeignKey('user.id',ondelete="CASCADE"),unique=True)

    def __repr__(self):
        return f"<Profile: {self.username}"
    

# with app.app_context():
#     db.create_all()




if __name__ == "__main__":
    app.run(debug=True)
