# import SentimentIntensityAnalyzer class from vaderSentiment.vaderSentiment module.
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd

# Import dataset
tweet_list = pd.read_csv('trumptweets.csv')
pos_score = []
neg_score = []
neu_score = []
overall_score = []


for tweet in tweet_list['content']:
    sid_obj = SentimentIntensityAnalyzer()
    sentiment_dict = sid_obj.polarity_scores(tweet)

    if sentiment_dict['compound'] >= 0.05:
        mood = 'positive'
    elif sentiment_dict['compound'] <= - 0.05:
        mood = 'negative'
    else:
        mood = 'neutral'
    overall_score.append(mood)


tweet_list.to_csv('vader_1.csv', index=False, encoding='utf-8-sig')
