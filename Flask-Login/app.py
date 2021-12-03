import os
from flask import Flask
from flask import render_template, request, redirect, session
from flask_wtf.csrf import CSRFProtect
from forms import RegisterForm, LoginForm

from models import db
from models import User

app = Flask(__name__)

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        session["userid"] = form.data.get("userid")
        
        userid = form.data.get("userid")
        password = form.data.get("password")
        
        print(userid, password)
    
        return redirect('/')
    
    return render_template("login.html", form=form)

@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User()
        user.userid = form.data.get("userid")
        user.username = form.data.get("username")
        user.password = form.data.get("password")
        
        db.session.add(user)
        db.session.commit()
    
        return redirect('/')
    
    return render_template("register.html", form=form)

@app.route('/')
def hello_world():
    userid = session.get("userid", None)
    return render_template("index.html", userid=userid)

if __name__ == "__main__":
    basedir = os.path.abspath(os.path.dirname(__file__))
    dbfile = os.path.join(basedir, "db.sqlite")

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + dbfile
    app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"] = True
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = "absdfaweghrhrlsasdfasdgdsa"
    app.config["SESSION_COOKIE_SECURE"] = True
    
    csrf = CSRFProtect()
    csrf.init_app(app)
    
    db.init_app(app)
    db.app = app
    db.create_all()
    
    app.run()