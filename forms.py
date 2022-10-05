from flas_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRquired,Length,EqualTo

class RegistrationForm(FlaskForm):
       username = StringField(label='Username',validators=[DataRequired(),Length(min=3,max=30)])
       password = PasswordField(label='Password',,validators=[DataRequired(),Length(min=6,max=30)])
       confirm_password= PasswordField(label='Confirm Password',validators=[DataRequired(),EqualTo('password')]
       submit= SubmitField(label='Sign Up')
