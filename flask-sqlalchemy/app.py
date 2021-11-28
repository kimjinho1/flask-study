from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from datetime import datetime

basedir = os.path.abspath(os.path.dirname(__file__))
dbfile = os.path.join(basedir, "db.sqlite")

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///' + dbfile
# 트랜잭션
app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"] = True
# 경고 무시
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Model(db.Model):
    __tablename__ = 'test_table'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(12), unique=True)
    date = db.Column(db.DateTime, unique=True, default=datetime.utcnow)

db.create_all()

@app.route('/')
def hello_world():
    return "Hello World!"
