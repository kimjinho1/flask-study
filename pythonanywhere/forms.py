from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, EqualTo, ValidationError

from models import User

class RegisterForm(FlaskForm):

    class DuplicateId(object):
        def __init__(self, message=None):
            self.message = message
    
        def __call__(self, form, field):
            userid = field.data            
            user = User.query.filter_by(userid=userid).first()
            if user:
                raise ValidationError("Duplicate ID")

    class DuplicateUsername(object):
        def __init__(self, message=None):
            self.message = message
    
        def __call__(self, form, field):
            username = field.data
            user = User.query.filter_by(username=username).first()
            if user:
                raise ValidationError("Duplicate Username")
    
    userid = StringField("userid", validators=[DataRequired(), DuplicateId()],)
    username = StringField("username", validators=[DataRequired(), DuplicateUsername()])
    password = PasswordField("password", validators=[DataRequired(), EqualTo("repassword")])
    repassword = PasswordField("repassword", validators=[DataRequired()])
    
    
class LoginForm(FlaskForm):

    class UserId(object):
        def __init__(self, message=None):
            self.message = message
    
        def __call__(self, form, field):
            userid = field.data
            user = User.query.filter_by(userid=userid).first()
            if not user:
                raise ValidationError("ID does not exist")
    
    class UserPassword(object):
        def __init__(self, message=None):
            self.message = message
        
        def __call__(self, form, field):
            userid = form["userid"].data
            password = field.data
            
            user = User.query.filter_by(userid=userid).first()
            if user:
                if user.password != password:
                    raise ValidationError("Worng password")
            
    userid = StringField("userid", validators=[DataRequired(), UserId()])
    password = PasswordField("password", validators=[DataRequired(), UserPassword()])
    