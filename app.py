''' Define parameters to run App '''
import os
from flask import Flask, render_template, request
from flask.ext.bootstrap import Bootstrap
from forms import TextForm
# from process.classification import Classify
from process.process_text import clean
import requests
import json

# Create flask application
app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

# Setup Database, bootstrap, login, analytics
Bootstrap(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    ''' Get Data from text form and classify '''
    txt = None
    form = TextForm()
    answer = None
    if request.method == "POST":
        txt = request.form['text']
        data = clean(txt)
        data = json.dumps(data)
        r = requests.post('https://sandbox.yhathq.com/lwgray@gmail.com/models/NbClassifier', data=data, auth=('lwgray@gmail.com', '0157a549d06212497e06dd50571adda0'))
        answer = r.text
        answer = json.loads(answer)
        answer = answer['result']
        return render_template('index.html', form=form, answer=answer, txt=data)
    else:
        return render_template('index.html', form=form, answer=answer, txt=txt)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
