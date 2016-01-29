'''Extract NAICS Sector Information'''
# coding: utf-8
import urllib
from lxml import etree
import json
import requests
from lxml import html
import pickle
from tqdm import tqdm

HTMLPARSER = etree.HTMLParser()
XMLPARSER = etree.XMLParser(remove_blank_text=True)

def get_first_level(): 
    '''Obtain first level sector information'''
    url = "http://www.census.gov/cgi-bin/sssd/naics/naicsrch?chart=2012"
    response = urllib.urlopen(url)
    tree = etree.parse(response, HTMLPARSER)
    title = tree.xpath('*//tr/td/a/@title')
    title = title[:20]
    title = [x[16:] for x in title]
    link = tree.xpath('*//tr/td/a/@href')
    link = link[:20]
    link = ['http://census.gov{0}'.format(x) for x in link]
    text = tree.xpath('*//tr/td/a/text()')
    text = text[:20]
    text = [str(x) for x in text]
    data = zip(title, link, text)
    pickle.dump(data, open('pickle/naics_corpus_level1.p', 'w'))
    return


def get_second_level(level_one_info):
    '''Obtain second level sector information'''
    dataList = []
    dataDict = {}
    for info in tqdm(level_one_info):
        url = info[1]
        key = info[2]
        title = info[0]
        response = urllib.urlopen(url)
        tree = etree.parse(response, HTMLPARSER)
        title1 = tree.xpath('*//tr/td/b[2]/text()')
        title1 = [str(x) for x in title1]
        title2 = tree.xpath('*//tr/td/text()')
        title2 = [x.strip() for x in title2 if x.strip() != ""]
        link1 = tree.xpath('*//tr/td/b/a/@href')
        link1 = ['http://census.gov{0}'.format(x) for x in link1]
        link2 = tree.xpath('*//tr/td/a/@href')
        link2 = ['http://census.gov{0}'.format(x) for x in link2]
        text1 = tree.xpath('*//tr/td/b/a/text()')
        text1 = [str(x) for x in text1]
        text2 = tree.xpath('*//tr/td/a/text()')
        text2 = [str(x) for x in text2]
        data1 = zip(title1, link1, text1)
        data2 = zip(title2, link2, text2)
        data = data1 + data2
        data = sorted(data, key=lambda tup: tup[2])
        dataList.append(data)
        dataDict[key] = data
    pickle.dump(dataDict, open('pickle/naics_corpus_level2.p', 'w'))
    return dataDict


def get_third_level(level_two_info):
    ''' Obtain descriptive info for the sectors'''
    data = {}
    for key, value in level_two_info.iteritems():
        for info in value:
            url = info[1]
            sector_id = info[2]
            title = info[0]
            page = requests.get(url)
            tree = html.fromstring(page.content)
            root = tree.get_element_by_id('middle-column')
            # Removes Excluded from Description
            text = root.text_content().split('Excluded')[0]
            text = text.split('\n')
            text = [x for x in text if x.strip()]
            text = [x.strip() for x in text]
            try:
                data[key][sector_id] = {title:text}
            except KeyError:
                data[key] = {sector_id:{title:text}}
    pickle.dump(data, open('pickle/naics_corpus_level3.p', 'w'))
    return data


if __name__ == '__main__':
    data2 = pickle.load(open('pickle/naics_corpus_level2.p', 'r'))
    data3 = get_third_level(data2)
    print data3.keys()
