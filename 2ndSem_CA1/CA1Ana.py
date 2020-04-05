import requests
from bs4 import BeautifulSoup

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

#print(response.content)

soup = BeautifulSoup(response.content, 'html.parser')

#print(soup.prettify())

print(soup.title.string)

# cells = soup.find_all('td')

#print(cells)

#for cell in cells: 
 #   print(cell.string)

def extract_island(cell):
    anchor = cell.find_all('a')
    print(anchor[0].string, end=',' )

def extract_county(cell):
    anchor = cell.find_all('a')
    print(anchor[0].string, end=',')

def extract_population(cell):
    spans = cell.find_all('span')
    txt = str(spans[0].string).replace(',', '')
    print(txt, end=',')
    
def extract_area(cell):
    txt = str(cell.get_text())
    km2idx = txt.index('km2') - 1
    txt = txt[0:km2idx]
    print(txt, end=',')
    
def extract_higest_point(cell):
    txt = str(cell.get_text())
    m2idx = txt.index('m') - 1
    txt = txt[0:m2idx]
    print(txt, end=',')
    
def extract_population_density(cell):
    txt = str(cell.get_text())
    km2idx = txt.index('km2') -1
    txt = txt[0:(km2idx)]
    print(txt, end=',')
    
 
def extract_data(row):
    cells = row.find_all('td')
    if len(cells) > 3:
        extract_island(cells[1])
        extract_county(cells[2])
        extract_population(cells[3])
        extract_area(cells[4])
        extract_higest_point(cells[5])
        extract_population_density(cells[6])
        print('')
 
 
 
t_islands = soup.find_all('table')
#print(len(t_islands))

#print(t_islands[1])

table_islands = t_islands[1]

table_body = table_islands.find_all('tbody')

table_rows = table_body[0].find_all('tr')

for row in table_rows:
    extract_data(row)
    



