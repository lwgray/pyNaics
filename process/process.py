#process
import cPickle as pickle
from prettyprint import prettyprint

class Process(object):
    def __init__(self, fname=''):
        self.fname = fname
        if fname == '':
            raise IOError("Please  enter name of pickled file,\
                          ie text = Load('pickles/example.p')")
        self.fulltext = None
        self.header = False
        self.description = {}
        pass

    def load(self):
        text = pickle.load(open(self.fname, 'rb'))
        self.fulltext = text.split('\n')
        return self.fulltext

    def get_sectors(self):
        if self.fulltext is None:
            corpus = self.load()
        else:
            corpus = self.fulltext
        if len(corpus) > 2:
            subject = ''
            for line in corpus:
                line = line.strip()
                if '--' in line and line[-1] == 'T':
                    sector_title = line.rstrip()
                if '\xe2' in line and line[-1] == 'T':
                    sector_title = line.rstrip()
                if 'Sector' in line and line[-1] == 'T':
                    sector_title = line.rstrip()
                if 'The Sector as a Whole' in line:
                    self.description[sector_title] = subject
                    subject = ''
                    self.header = True
                else:
                    if not self.header:
                        continue
                    else:
                        subject += line
            return self.description
        else:
            raise IOError('Text is too short')
        return

if __name__ == '__main__':
    text = Process('../pickle/naics.p')
    data = text.get_sectors()
    print len(data), '\n'
    for key, value in data.iteritems():
        print key
