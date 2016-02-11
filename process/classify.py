# coding: utf-8
from classification import Classify
import nltk

a = Classify()
data = a.compose_high_level_samples()
test = ''
with open('../txt/test3.txt', 'r') as txt:
    for line in txt:
        test += line
test1 = {'sentence': test}
trainset = [({'sentence': value}, key) for key, value in data.iteritems()]
classifier = nltk.NaiveBayesClassifier.train(trainset)
print classifier.classify(test1)
