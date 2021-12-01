# Flask-SQLAlchemy

## Python ORM인 flask-sqlalchemy를 통해 flask 안에서 데이터베이스를 쉽게 관리할 수 있다.

#### ORM(Object-Relational Mapping): 데이터베이스와 객체 지향 프로그래밍 언어 간의 호환되지 않는 데이터를 변환하는 프로그래밍 기법

**이와 같은 ORM을 사용하면 SQL을 사용하지 않고 Python만으로도 객체 간의 관계를 풀어낼 수가 있다.**  
**-> 개발자가 객체지향적인 코드 덕분에 비즈니스 로직에 더 집중을 할 수 있다.**  

**아래 코드와 같은 방식으로 데이터베이스를 쉽게 생성할 수 있다.**  

```python3
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.String(16))
    password = db.Column(db.String(32))
    date = db.Column(db.DateTime, default=datetime.utcnow)

basedir = os.path.abspath(os.path.dirname(__file__))
dbfile = os.path.join(basedir, "db.sqlite")

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///' + dbfile
# 경고 무시용
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
db.app = app
db.create_all()
```
