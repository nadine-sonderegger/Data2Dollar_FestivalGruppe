"""
Partly taken from: https://www.geeksforgeeks.org/python-sentiment-analysis-using-vader/ and https://www.datacareer.ch/blog/sentiment-analysis-in-python/
"""
# import SentimentIntensityAnalyzer class from vaderSentiment.vaderSentiment module.
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd

# Import dataset
tweet_list = pd.read_csv('trumptweets_1.csv')
pos_score = []
neg_score = []
neu_score = []
overall_score = []

sid_obj = SentimentIntensityAnalyzer()

for tweet in tweet_list['content']:
    sentiment_dict = sid_obj.polarity_scores(tweet)
    neg = sentiment_dict['neg']
    pos = sentiment_dict['pos']
    neu = sentiment_dict['neu']

    if sentiment_dict['compound'] >= 0.05:
        mood = 'positive'
    elif sentiment_dict['compound'] <= - 0.05:
        mood = 'negative'
    else:
        mood = 'neutral'

    overall_score.append(mood)
    pos_score.append(pos)
    neg_score.append(neg)
    neu_score.append(neu)

tweet_list['pos_score'] = pos_score
tweet_list['neg_score'] = neg_score
tweet_list['neu_score'] = neu_score
tweet_list['overall_score'] = overall_score

tweet_list.drop(tweet_list.columns[5:10], axis=1, inplace=True)

print(tweet_list.head())

tweet_list.to_csv('vader_3.csv', index=False, encoding='utf-8-sig')
