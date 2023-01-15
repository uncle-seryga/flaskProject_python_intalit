from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField
from wtforms.validators import DataRequired


class LoginForms(FlaskForm):
    login = StringField('Login', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign in')


class RegistrationForm(FlaskForm):
    login = StringField('Login', validators=[DataRequired()])
    password_1st = PasswordField('Enter password', validators=[DataRequired()])
    password_2nd = PasswordField('Confirm password', validators=[DataRequired()])
    name = StringField('Login', validators=[DataRequired()])
    surname = StringField('Login', validators=[DataRequired()])
    dob = DateField('Login', validators=[DataRequired()])
    tg_acc = StringField('Login')
    submit = SubmitField('Sign Up')
