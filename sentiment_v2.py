import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt
import nltk
import nltk.corpus as corp
from nltk import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from wordcloud import WordCloud, STOPWORDS
from textblob import TextBlob

# Import dataset
tweet_list = pd.read_csv('trumptweets_downloaded.csv')

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
for tweet in tweet_list['content']:
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


tweet_list['sentimental_score'] = scores
tweet_list['sentiment_status'] = status
tweet_list['subjectivity'] = sub
tweet_list.drop(tweet_list.columns[4:9], axis=1, inplace=True)

print(tweet_list.head())

positive = len(tweet_list[tweet_list['sentiment_status'] == 'positive'])
negative = len(tweet_list[tweet_list['sentiment_status'] == 'negative'])
neutral = len(tweet_list[tweet_list['sentiment_status'] == 'neutral'])

tweet_list.to_csv('sentiment_v2.csv', index=False, sep=';')
