''' Define parameters to run App '''
import os
from flask import Flask, render_template, request
from flask.ext.bootstrap import Bootstrap
from forms import TextForm
# from process.classification import Classify
from process.process_text import clean
import cPickle as pickle
import nltk

# Create flask application
app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

# Setup Database, bootstrap, login, analytics
Bootstrap(app)
with open('pickle/nb_classifier.cp', 'r') as csf:
    nb_classifier = pickle.load(csf)


@app.route('/', methods=['GET', 'POST'])
def index():
    ''' Get Data from text form and classify '''
    txt = None
    form = TextForm()
    answer = None
    category = {'11': 'Agriculture, Forestry, Fishing and Hunting',
                '21': 'Mining, Quarrying, and Oil and Gas Extraction',
                '22': 'Utilities',
                '23': 'Construction',
                '31-33': 'Manufacturing',
                '42': 'Wholesale Trade',
                '44-45': 'Retail Trade',
                '48-49': 'Transportation and Warehousing',
                '51': 'Information',
                '52': 'Finance and Insurance',
                '53': 'Real Estate and Rental and Leasing',
                '54': 'Professional, Scientific, and Technical Services',
                '55': 'Management of Companies and Enterprises',
                '56': 'Administrative and Support and Waste Management and Remediation Services',
                '61': 'Education Services',
                '62': 'Health Care and Social Assistance',
                '71': 'Arts, Entertainment, and Recreation',
                '72': 'Accomodation and Food Services',
                '81': 'Other SErvies(except Public Administration)',
                '92': 'Public Administration'}

    if request.method == "POST":
        txt = request.form['text']
        txt = clean(txt)
        answer = nb_classifier.classify(txt)
        answer = category[answer]
        print answer
    return render_template('index.html', form=form, answer=answer, txt=txt)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

'''
@app.route('/', methods=['GET', 'POST'])
def index():
'''
'''
    Get Data from text form
'''
'''
    form = TextForm()
    test = ''
    answer = None
    if request.method == "POST":
        txt = request.form['text']
        a = Classify()
        data = a.compose_high_level_samples()
        for line in txt:
            test += line
        test1 = {'sentence': test}
        trainset = [({'sentence': value}, key) for key, value in data.iteritems()]
        classifier = nltk.NaiveBayesClassifier.train(trainset)
        answer = classifier.classify(test1)
        print answer
    return render_template('index.html', form=form, answer=answer)
'''
