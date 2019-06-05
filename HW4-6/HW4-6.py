# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 00:38:30 2019

@author: user
"""

# -*- coding: utf-8 -*
import requests
from bs4 import BeautifulSoup
import types
r = requests.get("https://8book.com/books/novelbook_98524.html")

soup = BeautifulSoup(r.text, "html.parser")

#print(soup)
link = []
for table in soup.find_all("table", {'class' : 'episodelist'}):
    for tr in table.find_all('tr'):
        for a in tr.find_all('a', href=True):
            link.append('https://8book.com' + a['href'])
novel=''
for i in range(len(link)):
    r = requests.get(link[i])
    r.encoding = 'big5'
    soup = BeautifulSoup(r.text, "html.parser")
    st = soup.find('p')
    
    for s in st:
        novel += str(s).replace('(adsbygoogle = window.adsbygoogle || []).push({});', '')
f = open('novel/novel_1.txt','wb')
#f.write(novel.encode('utf-8'))
f.write(novel.replace('<br/>', '').encode('utf-8'))
f.close()