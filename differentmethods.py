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

# follower_ids
follower_ids = api.followers_ids(screen_name='realDonaldTrump')
print(follower_ids)

# user_timeline
timeline = api.user_timeline(user_id=25073877, count=200)
