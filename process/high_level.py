import cPickle as pickle
from monkeylearn import MonkeyLearn
ml = MonkeyLearn('87f134f1e1cc67bba8efb449a9e67f68de5a778a')
module_id = 'cl_RfmStLjx'


class HighLevel(object):
    def __init__(self):
        self.final = {}
        self.samples = []
        return

    def compose_high_level_samples(self):
        with open('pickle/naics_corpus_level3.p', 'r') as txt:
            data = pickle.load(txt)
            for i in data.keys():
                key = data[i][i].keys()[0]
                value = data[i][i][key]
                self.final[key] = ' '.join(value)
        return

    def create_categories(self):
        info = ml.classifiers.detail(module_id)
        parent_id = info.result['sandbox_categories'][0]['id']
        if not self.final:
            self.compose_high_level_samples()
        for key, value in self.final.iteritems():
            ml.classifiers.categories.create(module_id, key, parent_id)
        view = ml.classifiers.detail(module_id)
        print view.result
        return

    def create_samples(self):
        if not self.final:
            self.compose_high_level_samples()
        if self.samples:
            self.samples = []
        info = ml.classifiers.detail(module_id)
        result = info.result
        for item in result['sandbox_categories']:
            if item['name'] in self.final.keys():
                value = self.final[item['name']]
                self.samples.append((value, item['id']))
        return

    def upload_samples(self):
        if not self.samples:
            self.create_samples()
        res = ml.classifiers.upload_samples(module_id, self.samples)
        return res.result
