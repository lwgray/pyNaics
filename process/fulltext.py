# coding: utf-8
import pickle
with open('../pickle/naics_corpus_level3.p', 'r') as txt:
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
print new_data.keys()
