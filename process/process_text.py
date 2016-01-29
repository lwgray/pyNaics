# coding: utf-8
import pickle
from nltk.corpus import stopwords
import re
from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures
import collections
import sys
from progress.bar import Bar


def load(pfile='naics_corpus_level3.p'):
    feats_list = []
    final_feats = None
    label_feats = collections.defaultdict(list)
    with open('../pickle/{0}'.format(pfile), 'r') as txt:
        data = pickle.load(txt)
    bar = Bar('Progress --> ', max=len(data))
    for label, value in data.iteritems():
        bar.next()
        for subnaics, feats in value.iteritems():
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
    bar.finish()
    with open('label_feats.p', 'w') as pk:
        pickle.dump(label_feats, pk)
    return label_feats


def clean(feats):
    text = re.sub("[^a-zA-Z]", " ", feats)
    words = text.lower().split()
    words = [w for w in words if len(w) > 1]
    words = bag_of_non_stopwords(words)
    words = bag_of_bigrams_words(words)
    return words


def bag_of_words(words):
    return dict([(word, True) for word in words])


def bag_of_non_stopwords(words, stopfile='english'):
    badwords = stopwords.words(stopfile)
    words = set(words) - set(badwords)
    words = list(words)
    return words


def bag_of_bigrams_words(words, score_fn=BigramAssocMeasures.chi_sq, n=200):
    bigram_finder = BigramCollocationFinder.from_words(words)
    bigrams = bigram_finder.nbest(score_fn, n)
    return bag_of_words(words + bigrams)


if __name__ == '__main__':
    sys.exit(load())
'''
def load(pfile='naics_corpus_level3.p'):
    with open('../pickle/{0}'.format(pfile), 'r') as txt:
        data = pickle.load(txt)
        new_data = {}
        for key, value in data.iteritems():
            new_data[key] = ''
            try:
                for a, b in value.iteritems():
                    try:
                        for c, d in b.iteritems():
                            new_data[key] += ' '.join(d)
                    except:
                        new_data[key] += ' '.join(b)
            except:
                print "oh no"
    return new_data
'''
'''
def clean(new_data):
    words = {}
    text = ''
    for key, value in new_data.iteritems():
        text = re.sub("[^a-zA-Z]", " ", value)
        words[key] = text.lower().split()
        word = words[key]
        words[key] = [w for w in word if len(w) > 1]
    return words
'''

'''
def bag_of_words_not_in_set(words, badwords):
    return bag_of_words(set(words) - set(badwords))
'''
'''
def bag_of_non_stopwords(words, stopfile='english'):
    badwords = stopwords.words(stopfile)
    return bag_of_words_not_in_set(words, badwords)
'''
