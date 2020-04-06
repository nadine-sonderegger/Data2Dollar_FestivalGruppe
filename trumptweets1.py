"""
Code partly taken from '<script src="https://gist.github.com/yanofsky/5436496.js"></script>'
"""

import tweepy
import datetime
import pandas as pd

ACCESS_TOKEN = '1230902594136084480-H4G2asyYOPsDoEAr9yDUNTaq6hZcOW'
ACCESS_SECRET = 'vXESwd7kUW0nwlsPIMld8SEBYZcqEUMCjGqB5efzH8YHL'
CONSUMER_KEY = 'dAiFKkSETLHJFXsVYzKaAzeCd'
CONSUMER_SECRET = '5iZEJ101m0FfdXP4e02waVDr7UwBuFwOYgiwrMtgczLSQljohQ'

# screen_name = 'realdonaldtrump'
# startDate = datetime.date(2019, 1, 1)
# endDate = datetime.date(2019, 12, 31)


def connect_to_twitter_OAuth():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth)
    return api


api = connect_to_twitter_OAuth()

screen_name = 'realdonaldtrump'
startDate = datetime.datetime(2019, 11, 1, 0, 0, 0)
endDate = datetime.datetime(2020, 4, 6, 0, 0, 0)

alltweets = []

# make initial request for most recent tweets (200 is the maximum allowed count)
new_tweets = api.user_timeline(screen_name, count=200,
                               exlude_replies=1, include_rts=0)

oldest = alltweets[-1].id - 1

for tweet in new_tweets:
    if tweet.created_at < endDate and tweet.created_at > startDate:
        alltweets.append(tweet)

while (new_tweets[-1].created_at > startDate):
    print("Last Tweet @", new_tweets[-1].created_at, " - fetching some more")
    new_tweets = api.user_timeline(screen_name, count=200,
                                   exlude_replies=1, include_rts=0, max_id=oldest)
    for tweet in new_tweets:
        if tweet.created_at < endDate and tweet.created_at > startDate:
            alltweets.append(tweet)
    oldest = alltweets[-1].id - 1

df = pd.DataFrame(alltweets, columns=['tweet_id', 'date_time', 'text'])
df.to_csv('trumptweets_3.csv', index=False, sep=';')
