from flask import flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, BooleanField
from wtforms.validators import DataRequired, Optional, InputRequired
  
class CalcForm(FlaskForm):
    swim_pace_time = StringField('Your swim pace per 100m', validators=[Optional()], description='HH:MM:SS')
    swim_race_time = StringField('Your swim time (total)', validators=[Optional()], description='HH:MM:SS')
    distance = IntegerField('Race distance in metres', validators=[DataRequired()])
    showsplits = BooleanField('Show splits')
    submit = SubmitField('Calculate')
