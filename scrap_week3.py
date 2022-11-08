from asyncore import write
from gettext import find
from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd
import re
import json

title_list = []
description_list = []
datetime_list = []
all_link_list = []
link_list = []

url = requests.get('https://www.healthline.com/health-news')
url.encoding = "uft-8"
soup = BeautifulSoup(url.text, 'html.parser') 


for i in range(20):
    for c in soup.find_all('ol',{'class':'css-1iruc8t'}):

        title_list.append([item.text for item in c.find_all('h2',{'class' : 'css-1jcjjjn'})][i])

        description_list.append([item.text for item in c.find_all('a',{'class' : 'css-2fdibo'})][i])

        datetime_list.append([item.text for item in c.find_all('div',{'class' : 'css-mmjpxh'})][i])

        for L in c.find_all("div",{'class':'css-8atqhb'}):
            all_link_list.append(str(L.find("a",{'class':'css-1a66jak'}).get("href")))     
        
        link_list.append(all_link_list[i])

data = {'Title' : title_list, 'Description' : description_list,'Date' : datetime_list, 'url' : link_list}
table = pd.DataFrame(data)
table['url'] = 'https://www.healthline.com'+ table['url']

table = table.to_dict('records')

print(table)