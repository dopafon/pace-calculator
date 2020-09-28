from flask import flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, BooleanField
from wtforms.validators import DataRequired, Optional, InputRequired
  
class SwimForm(FlaskForm):
    def validate(self):
        if self.swim_pace_time != '00:45:00':
            return False
        else:
            return True



    swim_pace_time = StringField('Your swim pace per 100m', validators=[Optional()], description='HH:MM:SS')
    swim_race_time = StringField('Your swim time (total)', validators=[Optional()], description='HH:MM:SS')
    distance = IntegerField('Race distance in metres', validators=[DataRequired()])
    showsplits = BooleanField('Show splits')
    submit = SubmitField('Calculate')

class BikeForm(FlaskForm):
    bike_pace_time = StringField('Your bike pace in km/h', validators=[Optional()], description='km/h')
    bike_race_time = StringField('Your bike time (total)', validators=[Optional()], description='HH:MM:SS')
    distance = IntegerField('Race distance in kilometres', validators=[DataRequired()])
    showsplits = BooleanField('Show splits')
    submit = SubmitField('Calculate')
