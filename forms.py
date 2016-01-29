from flask.ext.wtf import Form
from wtforms.fields import TextAreaField

class TextForm(Form):
    text = TextAreaField('Text')
