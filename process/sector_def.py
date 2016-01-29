from monkeylearn import MonkeyLearn

ml = MonkeyLearn('87f134f1e1cc67bba8efb449a9e67f68de5a778a')
module_id = 'cl_RfmStLjx'
res = ml.classifiers.detail(module_id)
parent_id = res.result['sandbox_categories'][0]['id']
description = {}

def naics_corpus():
    corpus = []
    with open('naics.txt', 'r') as data:
        for line in data:
            corpus.append(line)
    return corpus


def get_sector_description(corpus):
    for line in corpus:
        if 'The Sector as a Whole' in line:
            description[index] = subject
            subject = ''
            index += 1
        else:
            subject += line
    samples = [(value, key) for key, value in description.iteritems()]
    samples.pop(0)
    return samples


def get_sectors(corpus):
    sectors = {}
    subject = ''
    header = False
    description = {}
    for line in corpus:
        line = line.strip()
        if line[:6] == 'Sector' and line[-1] == 'T':
            sector_title = line.rstrip()
        if 'The Sector as a Whole' in line:
            description[sector_title] = subject
            subject = ''
            header = True
        else:
            if not header:
                continue
            else:
                subject += line
    return description
