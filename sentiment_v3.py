import pandas as pd
import matplotlib.pyplot as plt
import nltk
from nltk import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import LancasterStemmer, WordNetLemmatizer, PorterStemmer
#from wordcloud import WordCloud, STOPWORDS
from textblob import TextBlob

# Import dataset
tweet_list = pd.read_csv('trumptweets_downloaded.csv')

# understand structure of dataset
print(tweet_list.shape)
print(tweet_list.columns)

# removing columns which are not important for sentiment analysis
remove_columns = ['id', 'link', 'date', 'retweets', 'favorites', 'mentions', 'hashtags', 'geo']
df = pd.DataFrame(tweet_list.drop(remove_columns, axis=1, inplace=False))

df['content'].value_counts().plot(kind='bar')
