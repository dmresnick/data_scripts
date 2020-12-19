import dash
import dash_table
import pandas as pd
import dash_core_components as dcc


import urllib3

from bs4 import BeautifulSoup

class get_wikiInfoBox(object):
    """
    This class is created as the base to scrape infobox data from wikipedia
    pages.

    Methods return the info box data as a list and as a dict {'column':infobox data}

    This data can then be used to create dataframes, create tauples for mySQL upload.
    """

    def __init__(self, url, infobox):
        #super(, self).__init__()
        #self.name = name
        self.url = url
        self.infobox = infobox


            #infobox_list = infobox.get_infobox_list()

    def get_infobox_dict(self):
        req = urllib3.PoolManager()
        res = req.request('GET', self.url)

        soup = BeautifulSoup(res.data, 'html.parser')
        webpage_data = soup.find('table', {'class': f'infobox {self.infobox}'}).findAll('tr')


        while("" in webpage_data):
            webpage_data.remove("")

        infobox_list = []
        col_num_list = []
        col_num = 0

        for i in webpage_data:
            col_num += 1
            webpage_text = (i.get_text())
            infobox_list.append(webpage_text)
            col_num_list.append(f'column {col_num}:')
            infobox_list = [i for i in infobox_list if i]
            webpage_dict = dict(zip(col_num_list, infobox_list))

        return webpage_dict

    def get_infobox_list(self):
        req = urllib3.PoolManager()
        res = req.request('GET', self.url)

        soup = BeautifulSoup(res.data, 'html.parser')
        webpage_data = soup.find('table', {'class': f'infobox {self.infobox}'}).findAll('tr')
        #print(webpage_data)
        infobox_list = []

        for i in webpage_data:
            webpage_text = (i.get_text())
            infobox_list.append(webpage_text)

        return infobox_list




def create_infobox_obj(self):
    url_list = ['https://en.wikipedia.org/wiki/Chrysler_Building', 'https://en.wikipedia.org/wiki/Empire_State_Building']
    data_items = []
    for i in url_list:
        infobox = get_wikiInfoBox(i , 'vcard' )
        infoboxList = infobox.get_infobox_list()
        infoboxDict = infobox.get_infobox_dict()
        #items.append(infoboxList)
        data_items.append(infoboxDict)
    return data_items

def create_dataframe():
    df = pd.DataFrame(create_infobox_obj('self'))
    print('Object Created')
    print('Creating Data Frame')
    return(df)


print(create_dataframe())
