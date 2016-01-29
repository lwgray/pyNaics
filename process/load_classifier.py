from process_text import clean

with open('pickle/nb_classifier.p', 'r') as csf:
    nb_classifier = pickle.loads(csf)

s1 = 'Other Services (except Public Administration)'
s1 = clean(s1)
s1 = nb_classifier.classify(s1)
print s1
