from flask_wtf import FlaskForm
# file upload enable: FileField, file upload restriction: FileAllowed
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.models import User


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    # costume validator for username
    def validate_username(self, username):
        # print(":::::::::::::::::", username.data)
        # print(":::::::::::::::::", User.query.filter_by(username=username.data).first())
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username is already taken. Choose another things')

    # costume validator for email
    def validate_email(self, email):
        # print(":::::::::::::::::", email.data)
        # print(":::::::::::::::::", User.query.filter_by(email=email.data).first())
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('email is already taken. Choose another things')


class UpdateProfileForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    # profile pic update
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    # costume validator for username
    def validate_username(self, username):
        print("::::::::1:::::::::", username.data)
        print("::::::::2:::::::::", current_user.username)
        print("::::::::3:::::::::", User.query.filter_by(username=username.data).first())
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            print("::::::4:::::::::::", user)
            if user:
                raise ValidationError('Username is already taken. Choose another things')

    # costume validator for email
    def validate_email(self, email):
        print(":::::::::::::::::", email.data)
        print(":::::::::::::::::", User.query.filter_by(email=email.data).first())
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('email is already taken. Choose another things')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class PostForm(FlaskForm):
    # first param is legend
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    # to use route
    submit = SubmitField('Post')

