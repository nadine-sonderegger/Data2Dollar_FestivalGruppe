# Crawler Trump Tweet

import tweepy
import pandas as pd

ACCESS_TOKEN = '1230902594136084480-H4G2asyYOPsDoEAr9yDUNTaq6hZcOW'
ACCESS_SECRET = 'vXESwd7kUW0nwlsPIMld8SEBYZcqEUMCjGqB5efzH8YHL'
CONSUMER_KEY = 'dAiFKkSETLHJFXsVYzKaAzeCd'
CONSUMER_SECRET = '5iZEJ101m0FfdXP4e02waVDr7UwBuFwOYgiwrMtgczLSQljohQ'


def connect_to_twitter_OAuth():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth)
    return api


api = connect_to_twitter_OAuth()

# Get User Info
user = api.get_user('realdonaldtrump')
print(user.screen_name)
print(user.followers_count)

# Get Tweets
get_tweets = api.user_timeline('realdonaldtrump')
tweet_list = []
for tweet in get_tweets:
    tweet_id = tweet.id
    text = tweet.text
    tweet_list.append({'tweet_id': tweet_id, 'text': text})
df = pd.DataFrame(tweet_list, columns=['tweet_id', 'text'])

df.to_csv('trumptweet.csv', index=False, sep=':')
