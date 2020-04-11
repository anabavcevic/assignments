# Git repository: https://github.com/anabavcevic/assignments/tree/master/2ndSem_CA1

import requests
from bs4 import BeautifulSoup
from CA1Ana_Functions import *


headers = {
    'authority': 'en.wikipedia.org',
    'cache-control': 'max-age=0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
    'sec-fetch-dest': 'document',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'referer': 'https://www.google.com/',
    'accept-language': 'en-IE,en-US;q=0.9,en;q=0.8,bs;q=0.7',
    'cookie': 'GeoIP=IE:L:Dublin:53.33:-6.25:v4; enwikimwuser-sessionId=61917032f005424e885d; WMF-Last-Access=05-Apr-2020; WMF-Last-Access-Global=05-Apr-2020',
}

response = requests.get('https://en.wikipedia.org/wiki/List_of_inhabited_islands_of_Croatia', headers=headers)

soup = BeautifulSoup(response.content.decode('utf-8').encode('cp1252', 'ignore'), 'html.parser')

table_rows= extract_rows(soup)

print("Island,County,Population,Area,Highest Point,Population Density")

for row in table_rows:
    extract_data(row)
    



