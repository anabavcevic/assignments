# Git repository: https://github.com/anabavcevic/assignments/tree/master/2ndSem_CA1

import requests
from bs4 import BeautifulSoup


def extract_island(cell):
    anchor = cell.find_all('a')
    return anchor[0].string

def extract_county(cell):
    anchor = cell.find_all('a')
    return anchor[0].string

def extract_population(cell):
    spans = cell.find_all('span')
    txt = str(spans[0].string).replace(',', '')
    return txt
    
def extract_area(cell):
    txt = str(cell.get_text())
    km2idx = txt.index('km2') - 1
    txt = txt[0:km2idx]
    return txt
    
def extract_higest_point(cell):
    txt = str(cell.get_text())
    m2idx = txt.index('m') - 1
    txt = txt[0:m2idx]
    return txt
    
def extract_population_density(cell):
    txt = str(cell.get_text())
    km2idx = txt.index('km2') -1
    txt = txt[0:(km2idx)]
    return txt
    
 
def extract_data(row):
    cells = row.find_all('td')
    if len(cells) > 3:
        print(extract_island(cells[1]), end=',' )
        print(extract_county(cells[2]), end = ',')
        print(extract_population(cells[3]), end = ',')
        print(extract_area(cells[4]), end = ',')
        print(extract_higest_point(cells[5]), end = ',')
        print(extract_population_density(cells[6]), end = ',')
        print('')
 
def extract_rows(soup):
    t_islands = soup.find_all('table')
    table_islands = t_islands[1]
    table_body = table_islands.find_all('tbody')
    table_rows = table_body[0].find_all('tr')
    return table_rows
    
