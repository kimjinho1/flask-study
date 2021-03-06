from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, EqualTo

class RegisterForm(FlaskForm):
    userid = StringField("userid", validators=[DataRequired()])
    username = StringField("username", validators=[DataRequired()])
    password = PasswordField("password", validators=[DataRequired(), EqualTo("repassword")])
    repassword = PasswordField("repassword", validators=[DataRequired()])
    