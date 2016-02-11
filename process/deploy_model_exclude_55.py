import cPickle as pickle
from yhat import Yhat, YhatModel, preprocess
import os


username = os.environ['USERNAME']
yhat_key = os.environ['YHAT_KEY']
yhat_url = os.environ['YHAT_URL']

with open('../pickle/nb_classifier_exclude_55.cp', 'r') as clf:
    nb_classifier = pickle.load(clf)


class NbClassifier(YhatModel):
    @preprocess(in_type=dict, out_type=str)
    def execute(self, data):
        answer = nb_classifier.classify(data)
        category = {'11': 'Agriculture, Forestry, Fishing and Hunting',
                    '21': 'Mining, Quarrying, and Oil and Gas Extraction',
                    '22': 'Utilities',
                    '23': 'Construction',
                    '31-33': 'Manufacturing',
                    '42': 'Wholesale Trade',
                    '44-45': 'Retail Trade',
                    '48-49': 'Transportation and Warehousing',
                    '51': 'Information',
                    '52': 'Finance and Insurance',
                    '53': 'Real Estate and Rental and Leasing',
                    '54': 'Professional, Scientific, and Technical Services',
                    '55': 'Management of Companies and Enterprises',
                    '56': 'Administrative and Support and Waste Management and Remediation Services',
                    '61': 'Education Services',
                    '62': 'Health Care and Social Assistance',
                    '71': 'Arts, Entertainment, and Recreation',
                    '72': 'Accomodation and Food Services',
                    '81': 'Other SErvies(except Public Administration)',
                    '92': 'Public Administration'}
        answer = category[answer]
        return answer

yh = Yhat(username, yhat_key, yhat_url)

yh.deploy("NbClassifier", NbClassifier, globals())
