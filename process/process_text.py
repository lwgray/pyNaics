''' Classify text into NAICS Categories '''
import cPickle as pickle
from nltk.corpus import stopwords
import re
from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures
import collections
from progress.bar import Bar
from gensim.models import Phrases


def label_feats_from_corpus(pfile='naics_corpus_level3.p'):
    '''
    Creates a list of labeled feature sets.
    This list is of the form [(featureset, label)],
    where the featureset variable is a dict and label
    is the known class label for the featureset.
    '''
    feats_list = []
    final_feats = None
    label_feats = collections.defaultdict(list)
    with open('../pickle/{0}'.format(pfile), 'r') as txt:
        data = pickle.load(txt)
    progressbar = Bar('Progress --> ', max=len(data))
    for label, value in data.iteritems():
        progressbar.next()
        for _, feats in value.iteritems():
            if isinstance(feats, dict):
                for x, y in feats.iteritems():
                    if isinstance(y, list):
                        for item in y:
                            feats_list.append(item.strip('T'))
                        final_feats = " ".join(feats_list)
                        final_feats = clean(final_feats)
                        label_feats[label].append(final_feats)
                        feats_list = []
                        final_feats = ''
                    else:
                        print "Oh No!"
            for item in feats:
                feats_list.append(item.strip('T'))
            final_feats = " ".join(feats_list)
            final_feats = clean(final_feats)
            label_feats[label].append(final_feats)
            feats_list = []
            final_feats = ''
    progressbar.finish()
    return label_feats


def clean(feats):
    ''' preprocess and clean text '''
    text = re.sub("[^a-zA-Z]", " ", feats)
    words = text.lower().split()
    words = [w for w in words if len(w) > 1]
    words = bag_of_non_stopwords(words)
    words = bag_of_bigrams_words(words)
    return words


def bag_of_words(words):
    '''
    return words as a dict with
    each word set as a key
    and the value equal to True
    '''
    return dict([(word, True) for word in words])


def bag_of_non_stopwords(words, stopfile='english'):
    ''' remove standard stop words '''
    badwords = stopwords.words(stopfile)
    words = [w for w in words if w not in badwords]
    # words = set(words) - set(badwords)
    # words = list(words)
    return words


def bag_of_bigrams_words(words):
    ''' add bigrams '''
    bigrams = Phrases()
    bigrams.add_vocab([words])
    bigrams = list(bigrams[words])
    return bag_of_words(words + bigrams)


def bag_of_bigrams_words_old(words, score_fn=BigramAssocMeasures.chi_sq, num=200):
    ''' add bigrams '''
    bigram_finder = BigramCollocationFinder.from_words(words)
    bigrams = bigram_finder.nbest(score_fn, num)
    return bag_of_words(words + bigrams)


def split_label_feats(lfeats, split=0.75):
    ''' split label_feats into training and test sets '''
    train_feats = []
    test_feats = []
    for label, feats in lfeats.items():
        cutoff = int(len(feats) * split)
        train_feats.extend([(feat, label) for feat in feats[:cutoff]])
        test_feats.extend([(feat, label) for feat in feats[cutoff:]])
    return train_feats, test_feats


if __name__ == '__main__':
    lfeats = label_feats_from_corpus()
    train_feats, test_feats = split_label_feats(lfeats, split=0.75)
    print len(train_feats)
    print len(test_feats)
