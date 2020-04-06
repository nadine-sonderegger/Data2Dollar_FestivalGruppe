"""
Code partly taken from '<script src="https://gist.github.com/yanofsky/5436496.js"></script>'
"""

# General:
import tweepy           # To consume Twitter's API
import pandas as pd     # To handle data
import numpy as np      # For number computing

# For plotting and visualization:
from IPython.display import display
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib

ACCESS_TOKEN = '1230902594136084480-H4G2asyYOPsDoEAr9yDUNTaq6hZcOW'
ACCESS_SECRET = 'vXESwd7kUW0nwlsPIMld8SEBYZcqEUMCjGqB5efzH8YHL'
CONSUMER_KEY = 'dAiFKkSETLHJFXsVYzKaAzeCd'
CONSUMER_SECRET = '5iZEJ101m0FfdXP4e02waVDr7UwBuFwOYgiwrMtgczLSQljohQ'

# screen_name = 'realdonaldtrump'
# startDate = datetime.date(2019, 1, 1)
# endDate = datetime.date(2019, 12, 31)


def twitter_setup():
    """
    Utility function to setup the Twitter's API
    with our access keys provided.
    """
    # Authentication and access using keys:
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    # Return API with authentication:
    api = tweepy.API(auth)
    return api


# We create an extractor object:
extractor = twitter_setup()

# We create a tweet list as follows:
tweets = extractor.user_timeline(screen_name="realDonaldTrump",
                                 count=200, exlude_replies=1, include_rts=0)
print("Number of tweets extracted: {}.\n".format(len(tweets)))

# We print the most recent 5 tweets:
print("5 recent tweets:\n")
for tweet in tweets[:5]:
    print(tweet.text)
    print()

# We create a pandas dataframe as follows:
data = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['Tweets'])

# We display the first 10 elements of the dataframe:
display(data.head(10))
