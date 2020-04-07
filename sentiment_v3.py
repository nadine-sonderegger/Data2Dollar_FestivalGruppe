import pandas as pd
import matplotlib.pyplot as plt
import nltk
from nltk import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from wordcloud import WordCloud, STOPWORDS
from textblob import TextBlob

# Import dataset
tweet_list = pd.read_csv('trumptweets_downloaded.csv')

# understand structure of dataset
print(tweet_list.shape)
print(tweet_list.columns)

# removing columns which are not important for sentiment analysis
remove_columns = ['id', 'link', 'date', 'retweets', 'favorites', 'mentions', 'hashtags', 'geo']
df = pd.DataFrame(tweet_list.drop(remove_columns, axis=1, inplace=False))

# Checking shape
print(df.shape)


# Lower Casing
# Change the reviews type to string
df['content'] = df['content'].astype(str)

# Lowercase all reviews
df['content'] = df['content'].apply(lambda x: " ".join(x.lower() for x in x.split()))

# Remove Punctuation
df['content'] = df['content'].str.replace('(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)', '')

# Remove STOPWORDS
stop = stopwords.words('english')
df['content'] = df['content'].apply(lambda x: " ".join(x for x in x.split() if x not in stop))

# Sentiment Score


def senti(x):
    return TextBlob(x).sentiment


df['senti_score'] = df['content'].apply(senti)
# print(df.senti_score.head()
# print(df.shape)
# print(df.columns)

df.to_csv('sentiment.csv', index=False, sep=';')

combined_list = pd.merge(tweet_list, df[['senti_score', 'content']], how='left', on='content')
combined_list.to_csv('tweetswithsentiment_left.csv', index=False, sep=';')
