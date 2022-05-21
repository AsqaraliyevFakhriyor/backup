 
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Integer, Column, ForeignKey
from sqlalchemy.orm import backref
from sqlalchemy.sql.sqltypes import JSON

db = SQLAlchemy()



class School(db.Model):
    __tablename__="school"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True)
    student = db.relationship("Student", cascade="all,delete", backref="school", lazy=True)

    def __init__(self, name):
        self.name = name

    def format(self) -> JSON:
        return {
            "name": self.name,
        }


class Student(db.Model):
    __tablename__="student"
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    school_id = Column(Integer, ForeignKey(School.id)) 

    def __init__(self, name):
        self.name = name

    def format(self) -> JSON:
        return {
            "name": self.name,
        }