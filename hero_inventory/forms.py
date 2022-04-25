from flask_wtf import  FlaskForm
from wtforms import StringField, PasswordField, SubmitField 
from wtforms.validators import DataRequired, Email


class UserSignUpForm(FlaskForm):
    first_name = StringField('First Name', validators= [DataRequired()])
    last_name = StringField('Last Name', validators= [DataRequired()])
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    submit_button = SubmitField()

class UserSigninForm(FlaskForm):
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    submit_button = SubmitField()
    
class HeroBuilderForm(FlaskForm):
    name = StringField('Name', validators= [DataRequired()])
    alias = StringField('Alias', validators= [DataRequired()])
    species = StringField('Species', validators= [DataRequired()])
    description = StringField('Description', validators= [DataRequired()])
    powers = StringField('Powers', validators= [DataRequired()])
    max_speed = StringField('Max Speed', validators= [DataRequired()])
    max_strength = StringField('Max Strength', validators= [DataRequired()])
    submit_button = SubmitField()


