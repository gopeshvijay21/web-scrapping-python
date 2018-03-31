# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 16:58:35 2018

@author: gopesh
"""

import csv
import requests
from bs4 import BeautifulSoup

url = 'http://espn.go.com/college-football/bcs/_/year/2013'
response = requests.get(url)
html = response.content

soup = BeautifulSoup((html), "lxml")
table = soup.find('table', attrs={'class': 'tablehead'})

list_of_rows = []
for row in table.findAll('tr')[0:]:
    list_of_cells = []
    for cell in row.findAll('td'):
        text = cell.text.replace('&nbsp;', '')
        list_of_cells.append(text)
    list_of_rows.append(list_of_cells)
    
with open("./Rankings.csv", "w") as outfile:
    csv_writer = csv.writer(outfile)
    csv_writer.writerows(list_of_rows)
