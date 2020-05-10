from textblob import TextBlob
import requests
from bs4 import BeautifulSoup

class Analysis:
    def __init__(self, term):
        self.term = term
        self.subjectivity = 0
        self.sentiment = 0

        self.url = 'https://www.google.com/search?q={0}&source)lnms&tbm=nws'.format(self.term)

    def run (self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, 'html.parser')
        headline_results = soup.find_all('div', class_='st')
        for h in headline_results:
            blob = TextBlob(text.get_text())
            self.sentiment += blob.sentiment.polarity / len(headline_results)
            self.subjectivity += blob.sentiment.subjectivity / len(headline_results)

a = Analysis('bitcoin')
a.run()
print(a.term, 'Subjectivity: ', a.subjectivity, 'Sentiment: ', a.sentiment)
