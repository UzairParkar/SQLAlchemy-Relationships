from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEM_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

'''For Better Stimulations
A. A Student can enroll in multiple Courses
B. A Course Can have Multiple Students
C. A Course Can have Multiple Instructors
D. An Instructor Can teach multiple courses'''



enroll = db.Table('enrollment',
                  db.Column('student_id',db.Integer,db.ForeignKey('student.id'),primary_key = True),
                  db.Column('course_id',db.Integer,db.ForeignKey('course.id'),primary_key = True)
                  )
teaching = db.Table('teaching',
                    db.Column('course_id',db.Integer,db.ForeignKey('course.id'),primary_key = True),
                    db.Column('instructor_id',db.Integer,db.ForeignKey('instructor.id'),primary_key = True)
                    )

class Student(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(30),nullable = True)
    roll_no = db.Column(db.Integer,nullable = False,unique = True)
    age = db.Column(db.Integer,nullable = False)
    courses = db.relationship('Course',secondary = enroll, backref = db.backref('students',lazy = 'dynamic'))

class Course(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(40),nullable = False)
    instructors = db.relationship('Instructor', secondary = teaching, backref = db.backref('courses',lazy = 'dynamic'))

class Instructor(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(40),nullable = False)
    age =  db.Column(db.Integer,nullable = True)





# with app.app_context():
#     db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
