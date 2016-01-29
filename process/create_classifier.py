# coding: utf-8
from process_text import label_feats_from_corpus
from process_text import split_label_feats
from nltk.classify import NaiveBayesClassifier
from process_text import clean

lfeats = label_feats_from_corpus()
train_feats, test_feats = split_label_feats(lfeats, split=0.75)

nb_classifier = NaiveBayesClassifier.train(train_feats)
