from flask_wtf import FlaskForm
from wtforms import (
StringField, 
PasswordField, 
TextAreaField, 
BooleanField, 
DateField, 
TimeField, 
SelectField, 
IntegerField
)
from wtforms.validators import DataRequired


class TodoForm(FlaskForm):
    genre_list = ['Belles-letres', 'History', 'Filosophy', 'Sci-fi', 'Technical']
    #id = IntegerField('No.',validators= [DataRequired()])
    title = StringField('Book title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    rent = BooleanField('Rent')
    date = DateField('Date added', validators=[DataRequired()])
    genre = SelectField('Genre', choices=genre_list, validators=[DataRequired()])
    first_name = StringField('Author first name', validators=[DataRequired()])
    last_name = StringField('Author last name', validators=[DataRequired()])