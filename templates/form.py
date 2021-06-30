from flask_wtf import FlaskForm
from wtform import StringField, PassswordField, SubmitField
from wtf.validators import InputRequired, Email
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Email()])
    password = PasswordField('Password', validators=[InputRequired()])
    login = SubmitField('Login')
