from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField, SelectField
from wtforms.validators import DataRequired


class CafeForm(FlaskForm):
    cafe_Name = StringField(label="Cafe Name", validators=[DataRequired()])
    cafe_Location = URLField(label="Cafe Location on Google Maps (URL)", validators=[DataRequired()])
    open_Time = StringField(label="Opening Time e.g. 8AM", validators=[DataRequired()])
    close_Time = StringField(label="Closing Time e.g. 5:30PM", validators=[DataRequired()])
    coffee_Rating = SelectField(label="Coffee Rating", validators=[DataRequired()],
                                choices=['☕️', '☕️☕️', '☕️☕️☕️', '☕️☕️️☕️☕️', '☕️☕️☕️☕️☕️'])
    wifi_Strength = SelectField(label="WiFi Strength Rating", validators=[DataRequired()],
                                choices=['❌', '💪', '💪💪', '💪💪💪', '💪💪💪💪', '💪💪💪💪💪'])
    power_Sockets = SelectField(label="Power Socket Availability", validators=[DataRequired()],
                                choices=['❌', '🔌', '🔌🔌', '🔌🔌🔌', '🔌🔌🔌🔌', '🔌🔌🔌🔌🔌'])
    submit = SubmitField("Submit")
