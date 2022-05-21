from logging import debug
import os
import bot
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin 
from flask_admin.contrib.sqla import ModelView
from flask_login import UserMixin


# setup for flask app

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'thesecretofapp'


db = SQLAlchemy(app)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80))
    user_tg_id = db.Column(db.Integer)

    def insert(self):
        db.session.add(self)
        db.session.commit(self)

class MyModelView(ModelView):
    def is_accessible(self):
        return True

admin = Admin(app)
admin.add_view(MyModelView(User, db.session))



if __name__ == '__main__':
    app.run(debug=True)
    