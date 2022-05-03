from flask_wtf import FlaskForm
from wtforms import validators
from wtforms.fields import *

class location_edit_form(FlaskForm):
#add back validator
    population = TextAreaField('Population',
    description = "Please add info about location population")
    #is_admin = BooleanField('Admin', render kw={'value':'1'})
    submit = SubmitField()

class csv_upload(FlaskForm):
    file = FileField()
    submit = SubmitField()