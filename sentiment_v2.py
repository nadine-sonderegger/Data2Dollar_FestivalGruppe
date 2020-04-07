from textblob import TextBlob
import nltk.corpus as corp
import nltk
import re
import matplotlib.pyplot as plt
import numpy as np
from pandas import ExcelFile
from pandas import ExcelWriter
import pandas as pd

# Excel Liste von gesamten Trump Tweets einlesen
excel_file = 'trumptweets_downloaded.xlsx'
tweet_data = pd.read_excel(excel_file)
#df = pd.open_excel('trumptweets_downloaded.xlsx')

# Zeigt Überschriften der Tabelle an
print('Column headings:', tweet_data.head())


# Liste der Tweets in dritter Spalte
# tweets = df['content']

stopword = corp.stopwords.words('english') + ['rt', 'https', 'co', 'u', 'go']


def clean_tweet(tweet):
    tweet = tweet.lower()
    filteredList = []
    global stopword
    tweetList = re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split()
    for i in tweetList:
        if i not in stopword:
            filteredList.append(i)
    return ' '.join(filteredList)


scores = []
status = []
sub = []
fullText = []
for tweet in tweet_data['content']:
    analysis = TextBlob(clean_tweet(tweet))
    fullText.extend(analysis.words)
    value = analysis.sentiment.polarity
    subject = analysis.sentiment.subjectivity
    if value > 0:
        sent = 'positive'
    elif value == 0:
        sent = 'neutral'
    else:
        sent = 'negative'
    scores.append(value)
    status.append(sent)
    sub.append(subject)


tweet_data['sentimental_score'] = scores
tweet_data['sentiment_status'] = status
tweet_data['subjectivity'] = sub
tweet_data.drop(tweet_data.columns[2:5], axis=1, inplace=True)

print(tweet_data.head())
