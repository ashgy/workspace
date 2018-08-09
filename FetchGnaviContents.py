from bs4 import BeautifulSoup
import requests
import openpyxl as px
import os

url = 'https://jsite.mhlw.go.jp/hokkaido-roudoukyoku/'
cls = 'm-headerMdrop__menu'

res = requests.get(url)
soup = BeautifulSoup(res.text, 'lxml')

#div = soup.find_all(class_ = cls)
#print(type(div))
section = soup.find_all(class_ = cls)

part = section[0].find_all('span')

for index, prt in enumerate(part):
    print(index)
    print (prt.prettify())
