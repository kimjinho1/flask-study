# Flask-WTF

### Flask-WTF 라이브러리를 사용하면 Python으로 Forms을 정의하고 HTML 탬플릿을 사용하여 랜더링 할 수 있다

### Forms의 유효성 검사와 CSRF 방지도 가능하다

**아래와 같은 방식으로 쉽게 Forms을 정의하고 유효성 검사를 할 수 있다.**

```python3
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, EqualTo

class RegisterForm(FlaskForm):
    userid = StringField('userid', validators=[DataRequired()])
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired(), EqualTo('repassword')])
    repassword = PasswordField('repassword', validators=[DataRequired()])
```

**아래와 같던 html을**

```html
<form method="POST">
    <div class="form-group">
        <label for="userid">아이디</label>
        <input type="text" class="form-control" id="userid" placeholder="아이디" name="userid">
    </div>
    <div class="form-group">
        <label for="username">사용자 이름</label>
        <input type="text" class="form-control" id="username" placeholder="사용자 이름" name="username">
    </div>
    <div class="form-group">
        <label for="password">비밀번호</label>
        <input type="password" class="form-control" id="password" placeholder="비밀번호" name="password">
    </div>
    <div class="form-group">
        <label for="re-password">비밀번호 확인</label>
        <input type="password" class="form-control" id="re-password" placeholder="비밀번호 확인" name="re-password">
    </div>
    <button type="submit" class="btn btn-primary">등록</button>
</form>
```

**이렇게 바꿔 사용할 수 있다. 훨씬 깔끔한 것 같다.**

```html
<form method="POST">
    {{ form.csrf_to }}
    <div class="form-group">
        {{ form.userid.label("아이디") }}
        {{ form.userid(class="form-control", placeholder="아이디") }}
    </div>
    <div class="form-group">
        {{ form.username.label("사용자 이름") }}
        {{ form.username(class="form-control", placeholder="사용자 이름") }}
    </div>
    <div class="form-group">
        {{ form.password.label("비밀번호") }}
        {{ form.password(class="form-control", placeholder="비밀번호") }}
    </div>
    <div class="form-group">
        {{ form.repassword.label("비밀번호 확인") }}
        {{ form.repassword(class="form-control", placeholder="비밀번호 확인") }}
    </div>
    <button type="submit" class="btn btn-primary">등록</button>
</form>
```
