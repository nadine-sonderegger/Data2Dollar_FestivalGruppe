# import SentimentIntensityAnalyzer class from vaderSentiment.vaderSentiment module.
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd

# Import dataset
tweet_list = pd.read_csv('trumptweets.csv')


def sentiment_scores(tweet):

    sid_obj = SentimentIntensityAnalyzer()
    sentiment_dict = sid_obj.polarity_scores(tweet)

    if sentiment_dict['compound'] >= 0.05:
        print("Positive")

    elif sentiment_dict['compound'] <= - 0.05:
        print("Negative")

    else:
        print("Neutral")
    return


if __name__ == "__main__":
    tweet = tweet_list['content']


tweet.to_csv('vader_1.csv', index=False, encoding='utf-8-sig')
