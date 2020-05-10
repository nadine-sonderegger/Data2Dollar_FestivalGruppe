import requests
from bs4 import BeautifulSoup

def pyGoogleSearch(word):
    address='http://www.google.com/search?q='
    newword = address + word
    page = requests.get(newword)
    import time
    time.sleep(10)
    soup = BeautifulSoup(page.content, 'html.parser')
    phrase_extract = soup.find('div', id="resultStats")
    val = int(phrase_extract.text.split(' ')[1].replace(',',''))
    print(val)

pyGoogleSearch('switzerland')
