# Crawler Trump Tweet

import tweepy
import csv
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

'''
# Get User Info
user = api.get_user('realdonaldtrump')
print(user.screen_name)
print(user.followers_count)
'''

# Get Tweets
tweets_list = []
get_new_tweets = api.user_timeline('realdonaldtrump', count = 200)
tweets_list.extend(get_new_tweets)

# save the id of the oldest tweet less one
#oldest = tweets_list[-1].id - 1

while len(get_new_tweets) > 0:
    get_new_tweets = api.user_timeline('realdonaldtrump', count = 200)

    # save most recent tweets
    tweets_list.extend(get_new_tweets)

    #oldest = tweets_list[-1].id - 1

    print("...%s tweets downloaded so far" % (len(tweets_list)))

outtweets = [[tweet.id_str, tweet.created_at,
              tweet.text.encode("utf-8")] for tweet in tweets_list]

f = pd.DataFrame(outtweets, columns=['id', 'created_at', 'text'])
f.to_csv('trumptweet5.csv', index = False, sep=',')
