# open-webpage.py

import urllib3

from bs4 import BeautifulSoup

class get_wikiInfoBox(object):
    """docstring for ."""

    def __init__(self, name, url, infobox):
        #super(, self).__init__()
        self.name = name
        self.url = url
        self.infobox = infobox


    def get_infobox_dict(self):
        req = urllib3.PoolManager()
        res = req.request('GET', self.url)

        soup = BeautifulSoup(res.data, 'html.parser')
        car_info_html = soup.find('table', {'class': f'infobox {self.infobox}'}).findAll('tr')



        infobox_list = []
        col_num_list = []
        col_num = 0

        for i in car_info_html:
            col_num += 1
            car_info_text = (i.get_text())
            infobox_list.append(car_info_text)
            col_num_list.append(f'column {col_num}:')
            car_info_dict = dict(zip(col_num_list, infobox_list))


        for k,v in car_info_dict.items():
            print(k, v)
        return car_info_dict

    def get_infobox_list(self):
        req = urllib3.PoolManager()
        res = req.request('GET', self.url)

        soup = BeautifulSoup(res.data, 'html.parser')
        car_info_html = soup.find('table', {'class': f'infobox {self.infobox}'}).findAll('td')

        infobox_list = []

        for i in car_info_html:
            car_info_text = (i.get_text())
            infobox_list.append(car_info_text)

        return infobox_list

infobox = get_wikiInfoBox('Civic 2nd generation', 'https://en.wikipedia.org/wiki/Albert_Einstein', 'biography vcard' )

infobox_dict = infobox.get_infobox_dict()

infobox_list = infobox.get_infobox_list()
print(infobox_dict)
print(infobox_list)
'''

url = 'https://en.wikipedia.org/wiki/Honda_Civic_(second_generation)'


response = urllib.request.urlopen(url)
webContent = response.read()

parese = urlparse('https://en.wikipedia.org/wiki/Honda_Civic_(second_generation)')

print(parese)

import urllib.request, urllib.error, urllib.parse


f = open('obo-t17800628-33.html', 'wb')
f.write(webContent)
f.close

print(webContent[0:300])
'''
