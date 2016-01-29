''' Define parameters to run App '''
import os
from flask import Flask, render_template, request
from flask.ext.bootstrap import Bootstrap
from forms import TextForm
from process.classification import Classify
import nltk

# Create flask application
app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

# Setup Database, bootstrap, login, analytics
Bootstrap(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    ''' Get Data from text form '''
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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
