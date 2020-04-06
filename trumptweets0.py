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


def get_all_tweets(screen_name, startDate, endDate):
    # Twitter only allows access to users most recent 3240 tweets with this method

    # authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth)

    # initialize a list to hold all the tweepy Tweets
    alltweets = []

    # make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(screen_name=screen_name, count=200,
                                   exlude_replies=1, include_rts=0)

    # save Tweets
    alltweets.extend(new_tweets)

    for tweet in new_tweets:
        if tweet.created_at < endDate and tweet.created_at > startDate:
            alltweets.append(tweet)

    while (new_tweets[-1].created_at > startDate):
        print("Last Tweet @", new_tweets[-1].created_at, " - fetching some more")
        new_tweets = api.user_timeline(screen_name=screen_name, count=200,
                                       exlude_replies=1, include_rts=0,
                                       max_id=new_tweets[-1].id)
        for tweet in new_tweets:
            if tweet.created_at < endDate and tweet.created_at > startDate:
                alltweets.append(tweet)

    df = pd.DataFrame(alltweets, columns=['tweet_id', 'date_time', 'text'])
    df.to_csv('trumptweets_3.csv', index=False, sep=';')


if __name__ == '__main__':
    # pass in the username of the account you want to download
    screen_name = 'realdonaldtrump'
    startDate = datetime.datetime(2019, 1, 1, 0, 0, 0)
    endDate = datetime.datetime(2019, 12, 31, 0, 0, 0)

"""
def get_all_tweets(screen_name):
    # Twitter only allows access to users most recent 3240 tweets with this method

    # authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth)

    # initialize a list to hold all the tweepy Tweets
    alltweets = []

    # make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(screen_name=screen_name, count=200,
                                   exlude_replies=1, include_rts=0)

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
                                       include_rts=0)

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
    df.to_csv('trumptweets_1.csv', index=False, sep=';')


if __name__ == '__main__':
    # pass in the username of the account you want to download
    get_all_tweets('realdonaldtrump')
"""
