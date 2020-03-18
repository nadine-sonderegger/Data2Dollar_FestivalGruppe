# Tweet Crawler

import tweepy
import pandas as pd
import csv

# Twitter API credentials
ACCESS_TOKEN = '1230902594136084480-H4G2asyYOPsDoEAr9yDUNTaq6hZcOW'
ACCESS_SECRET = 'vXESwd7kUW0nwlsPIMld8SEBYZcqEUMCjGqB5efzH8YHL'
CONSUMER_KEY = 'dAiFKkSETLHJFXsVYzKaAzeCd'
CONSUMER_SECRET = '5iZEJ101m0FfdXP4e02waVDr7UwBuFwOYgiwrMtgczLSQljohQ'

# authorize twitter, initialize tweepy
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

# initialize a list to hold all the tweepy Tweets
alltweets = []

# make initial request for most recent tweets(200 is the max allowed count)
new_tweets = api.user_timeline('realdonaldtrump', count=200)

# save most recent tweets
alltweets.extend(new_tweets)

# save the id of the oldest tweet less one
oldest = alltweets[-1].id - 1

# keep grabbing tweets until there are no tweets left to grab
while len(new_tweets) > 0:
    print('getting tweets before %s')

    # all subsiquent requests use the max_id param to prevent duplicates
    new_tweets = api.user_timeline('realdonaldtrump',
                                   count=200, max_id=oldest)

    # save most recent tweets
    alltweets.extend(new_tweets)

    # update the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1

    print("...%s tweets downloaded so far" % (len(alltweets)))

# transform the tweepy tweets into a 2D array that will populate the csv
"""
outtweets = [[tweet.id_str, tweet.created_at,
                  tweet.text.encode("utf-8")] for tweet in alltweets]
"""
outtweets = pd.DataFrame(alltweets, columns=[[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in alltweets ])

outtweets.to_csv('trumptweet.csv', index=False, sep=':')
"""
# write the csv
with open('%s_tweets.csv' % 'realdonaldtrump') as f:
    writer = csv.writer(f)
    writer.rows(["id", "created_at", "text"])
    writer.rows(outtweets)

pass
"""
