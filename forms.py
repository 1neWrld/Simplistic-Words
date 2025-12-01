from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, Email , EqualTo, ValidationError
from model import User
from database import db_session


#form to validate user input
class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(message='Title is required'),
                                             Length(min = 2, max = 100, message='Title must be between 2 and 100')])
    content = TextAreaField('Content', validators=[DataRequired(message='Content is required'),
                                                   Length(min = 10, message='Content must be at least 10 characters')])
    submit = SubmitField('Publish Post')

class RegistrationForm(FlaskForm):
    username = StringField('Username',
                          validators=[
                              DataRequired(),
                              Length(min=3, max=80, message='Username must be between 3 and 80 characters')
                          ])

    email = StringField('Email',
                       validators=[
                           DataRequired(),
                           Email(message='Please enter a valid email address')
                       ])

    password = PasswordField('Password',
                            validators=[
                                DataRequired(),
                                Length(min=6, message='Password must be at least 6 characters')
                            ])

    confirm_password = PasswordField('Confirm Password',
                                    validators=[
                                        DataRequired(),
                                        EqualTo('password', message='Passwords must match')
                                    ])

    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = db_session.query(User).filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username already taken. Please choose a different one.')

    def validate_email(self, email):
        user = db_session.query(User).filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email already taken. Please choose a different one.')

class  LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
