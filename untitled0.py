# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 15:31:39 2018

@author: Shuhaib
"""
import pandas as pd
import csv

from bs4 import BeautifulSoup
import requests
response = requests.get("http://www.amudirectory.com/ByCurrentCity.aspx?fltr=A%")

soup = BeautifulSoup(response.text, 'lxml')

d= soup.find_all('a')
dd=[]
for i in d:
    print(i.text)
    dd.append(i.text)
ddd= dd[48:225]
with open('kk.csv', 'w') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    for val in ddd:
        wr.writerow([val]) 
    
print(ddd)
