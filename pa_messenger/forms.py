from flask_wtf import FlaskForm
from werkzeug.datastructures import MultiDict
from wtforms import TextField, StringField
from wtforms.widgets import TextArea
from wtforms.validators import DataRequired, Length


class SendMessageForm(FlaskForm):
    message = StringField(
            'Message*',
            validators=[
                DataRequired(message="Message is required"),
                Length(min=1,
                    max=160,
                    message="Message must be between 1 and 160 characters")],
            widget=TextArea())
    imageUrl = TextField('Image URL', validators=[])

    def reset(self):
        blankData = MultiDict([('message', ''), ('imageUrl', '')])
        self.process(blankData)
