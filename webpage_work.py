import dash
import dash_table
import pandas as pd
import dash_core_components as dcc
from rich import print



import urllib3

from bs4 import BeautifulSoup

class get_table(object):


    def __init__(self, url):
        #super(, self).__init__()
        #self.name = name
        self.url = url
        #self.infobox = infobox


            #infobox_list = infobox.get_infobox_list()

    def get_scrape_dict(self):
        req = urllib3.PoolManager()
        res = req.request('GET', self.url)

        soup = BeautifulSoup(res.data, 'html.parser')
        webpage_data = soup.find('table', id ='table6').findAll('td')


        #print(webpage_data)
        #print(rows)

        infobox_list = []
        col_num_list = []
        col_num = 0

        for i in webpage_data:

            col_num += 1
            webpage_text = (i.get_text())
            #print(webpage_text)
            print(webpage_text)
            a = webpage_text.rstrip()
            print(a)
            infobox_list.append(webpage_text)
            col_num_list.append(f'column {col_num}:')
            infobox_list = [i for i in infobox_list if i]
            webpage_dict = dict(zip(col_num_list, infobox_list))

        return webpage_dict


    def get_scrape_list(self):
        req = urllib3.PoolManager()
        res = req.request('GET', self.url)

        soup = BeautifulSoup(res.data, 'html.parser')
        webpage_data = webpage_data = soup.find('table', id ='table6').findAll('td')
        #print(webpage_data)
        infobox_list = []

        for i in webpage_data:

            webpage_text = (i.get_text())

            infobox_list.append(webpage_text)

        return infobox_list

data_table = get_table('https://www.sfu.ca/~aheard/elections/1867-present.html')
scrape_list = data_table.get_scrape_list()



def clean_scrape_list():
    stripped_list = []
    for i in scrape_list:
        i = i.strip()
        stripped_list.append(i)

    while('' in stripped_list):
        stripped_list.remove('')

    clean_list_num = []
    clean_list = []
    col_num = -1
    for i in stripped_list:
        col_num += 1
        i = i.replace("\n", "")
        i = i.replace("\r", "")
        i = i.replace("   ", "")

        i = i.replace("\xa0", "")
        clean_list_num.append(f'{col_num} {i}')
        clean_list.append(i)


    return clean_list_num


clean_scrape_list()


my_list = (clean_scrape_list())

def get_list_by_year(start, end):
    year_list = my_list[0:40]

    return year_list

_2019 = get_list_by_year(0, 39)
_2015 = get_list_by_year(40, 74)
_2011 = get_list_by_year(75, 109)
_2008 = get_list_by_year(110, 144)
_2006 = get_list_by_year(145, 179)

print(_2019, _2015)

'''
_2004= get_list_by_year(180, 214)
_2000 = get_list_by_year(215, 39)
_2015 = get_list_by_year(40, 74)
_2019 = get_list_by_year(0, 39)
_2015 = get_list_by_year(40, 74)
_2019 = get_list_by_year(0, 39)
_2015 = get_list_by_year(40, 74)
_2019 = get_list_by_year(0, 39)
_2015 = get_list_by_year(40, 74)
_2019 = get_list_by_year(0, 39)
_2015 = get_list_by_year(40, 74)
_1896 = get_list_by_year(982, 1001)
_1891 = get_list_by_year(1002, 1020)
_1887 = get_list_by_year(1021, 1039)
_1882 = get_list_by_year(1040, 1055)
_1878 = get_list_by_year(1056, 1071)
_1874 = get_list_by_year(1072, 1087)
_1872 = get_list_by_year(1088, 1103)
_1867 = get_list_by_year(1104, 1118)

'''
