from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField(label='username', id='username_login', validators=[DataRequired()])
    password = PasswordField(label='password', id='password_login', validators=[DataRequired()])
