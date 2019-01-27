from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class SelectForm(FlaskForm):
    idi = StringField('idi', validators=[])
    name = StringField('name', validators=[])
    city = StringField('city', validators=[])
    rodn_gorod = StringField('Rodn_gorod', validators=[])
    sem_pol = StringField('sem_pol', validators=[])
    age = StringField('age', validators=[])
    #remember_me = BooleanField('Remember Me')
    submit = SubmitField('send')

class TableForm(FlaskForm):
    sub_id = SubmitField('ID')
    sub_name_p = SubmitField('Name')
    sub_gorod = SubmitField('City')
    sub_r_gorod= SubmitField('Rodn_gorod')
    sub_age = SubmitField('Age')
    sub_sem_pol = SubmitField('SemPol')
    sub_url = SubmitField('URL')
