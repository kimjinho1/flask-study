import os
from flask import Flask
from flask import render_template, request, redirect
from flask_wtf.csrf import CSRFProtect
from forms import RegisterForm

from models import db
from models import User

app = Flask(__name__)

@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User()
        user.userid = form.data.get("userid")
        user.username = form.data.get("username")
        user.password = form.data.get("password")
        
        db.session.add(user)
        db.session.commit()
        print("Success")
    
        return redirect('/')
    
    return render_template("register.html", form=form)

@app.route('/')
def hello_world():
    return render_template("index.html")

if __name__ == "__main__":
    basedir = os.path.abspath(os.path.dirname(__file__))
    dbfile = os.path.join(basedir, "db.sqlite")

    app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///' + dbfile
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