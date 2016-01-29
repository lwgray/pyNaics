import cPickle

class Classify(object):
    def __init__(self):
        self.final = {}
        self.samples = []
        return

    def compose_high_level_samples(self):
        ''' organize naics data by highest category '''
        with open('pickle/naics_corpus_level3.p', 'r') as txt:
            data = cPickle.load(txt)
            for i in data.keys():
                key = data[i][i].keys()[0]
                value = data[i][i][key]
                self.final[key] = ' '.join(value)
        return self.final


