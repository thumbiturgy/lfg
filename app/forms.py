from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email

class RegisterForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired()])
    submit = SubmitField('Register')

class SigninForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    submit = SubmitField('Register')

class PostForm(FlaskForm):
    body = StringField('body', validators=[DataRequired()])
    submit = SubmitField('Publish')

class UserSearchForm(FlaskForm):
    user = StringField('user', validators=[DataRequired()])
    submit = SubmitField('Search')

class CharacterForm(FlaskForm):
    name = StringField('character name', validators=[DataRequired()])
    hero_class = StringField('class')
    species = StringField('species/race')
    party_role = StringField('party role')
    saves = StringField('save proficiencies')
    personality_type = (' personality type')
    