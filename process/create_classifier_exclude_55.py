# coding: utf-8
import cPickle as pickle
from process_text_exclude_55 import label_feats_from_corpus
from process_text_exclude_55 import split_label_feats
from nltk.classify import NaiveBayesClassifier
from process_text_exclude_55 import clean

lfeats = label_feats_from_corpus()
train_feats, test_feats = split_label_feats(lfeats, split=0.75)

nb_classifier = NaiveBayesClassifier.train(train_feats)

print "writing classifier"
with open('../pickle/nb_classifier_exclude_55.cp', 'w') as nbp:
    pickle.dump(nb_classifier, nbp)


