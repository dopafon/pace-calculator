from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Optional

class CalcForm(FlaskForm):
    swim_pace_time = StringField('Your swim pace per 100m', validators=[Optional()])
    swim_race_time = StringField('Your swim time (total)', validators=[Optional()])
    distance = IntegerField('Race distance in metres', validators=[DataRequired()])
    submit = SubmitField('Calculate')

    def validate(self):
        if not self.swim_pace_time.data and not self.swim_race_time.data:
            msg = 'At least one of race or pace time must be set'
            self.swim_race_time.errors.append(msg)
            self.swim_pace_time.errors.append(msg)
            return False
        return True

