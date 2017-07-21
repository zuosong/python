#-*- coding:utf-8 -*-

from flask_wtf import Form
from wtforms import TextField,BooleanField,PasswordField,SubmitField, TextAreaField
from wtforms.validators import Required,Email,Length

class LoginForm(Form):
    user_name = TextField('user_name', validators = [Required(),Length(max=12)])
    #password = PasswordField('password', validators=[Required()])
    remember_me = BooleanField('Remember_me', default = False)
    submit = SubmitField('Log in')

class SignUpForm(Form):
    user_name = TextField('user_name',validators =[Required(),Length(max=15)])
    user_email = TextField('user_email',validators=[Email(),Required(),Length(max=128)])
    submit = SubmitField('Sign up')
