"""
Code partly taken from '<script src="https://gist.github.com/yanofsky/5436496.js"></script>'
"""

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

startSince = ('2014-10-01')
endUntil = ('2014-11-01')


def get_all_tweets(screen_name, startSince, endUntil):
    # Twitter only allows access to users most recent 3240 tweets with this method

    # authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth)

    # initialize a list to hold all the tweepy Tweets
    alltweets = []

    # make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(screen_name=screen_name, count=200,
                                   exlude_replies=1, include_rts=0, startSince=startSince, endUntil=endUntil)

    # save most recent tweets
    alltweets.extend(new_tweets)

    # save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1

    # keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:
        print('getting tweets before %s' % (oldest))

        # all subsiquent requests use the max_id param to prevent duplicates,
        # exlude_replies to not consider replies, include_rts to exlude retweets
        new_tweets = api.user_timeline(screen_name=screen_name, count=200,
                                       max_id=oldest, exlude_replies=1,
                                       include_rts=0, startSince=startSince, endUntil=endUntil)

        # save most recent tweets
        alltweets.extend(new_tweets)

        # update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1

        print("...%s tweets downloaded so far" % (len(alltweets)))

    print('Finished Downloading %s tweets' % screen_name)
    # transform the tweepy tweets into a 2D array that will populate the csv
    outtweets = [[tweet.id_str, tweet.created_at,
                  tweet.text.encode("utf-8")] for tweet in alltweets]

    df = pd.DataFrame(outtweets, columns=['tweet_id', 'date_time', 'text'])
    df.to_csv('trumptweets_8.csv', index=False, sep=';')


if __name__ == '__main__':
    # pass in the username of the account you want to download
    get_all_tweets('realdonaldtrump', '2014-10-01', '2014-11-01')
