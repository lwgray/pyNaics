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
username = os.environget("USERNAME")
pswd = os.environ.get('PSWD')

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
        r = requests.post('https://sandbox.yhathq.com/lwgray@gmail.com/models/NbClassifier', data=data, auth=(username, pswd))
        answer = r.text
        answer = json.loads(answer)
        answer = answer['result']
        return render_template('index.html', form=form, answer=answer, txt=data)
    else:
        return render_template('index.html', form=form, answer=answer, txt=txt)


@app.route('/model1', methods=['GET', 'POST'])
def model1():
    ''' Get Data from text form and classify '''
    txt = 'Enter Regulation Summary here....'
    form = TextForm()
    answer = 'The predicted category will appear here!'
    if request.method == "POST":
        txt = request.form['text']
        data = clean(txt)
        data = json.dumps(data)
        r = requests.post('https://sandbox.yhathq.com/lwgray@gmail.com/models/NbClassifier', data=data, auth=(username, pswd))
        answer = r.text
        answer = json.loads(answer)
        answer = answer['result']
        return render_template('model1.html', form=form, answer=answer, txt=data)
    else:
        return render_template('model1.html', form=form, answer=answer, txt=txt)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
