import cPickle as pickle
from yhat import Yhat, YhatModel, preprocess


with open('../pickle/nb_classifier.cp', 'r') as clf:
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

yh = Yhat(
    "lwgray@gmail.com",
    "0157a549d06212497e06dd50571adda0",
    "https://sandbox.yhathq.com"
)

yh.deploy("NbClassifier", NbClassifier, globals())
