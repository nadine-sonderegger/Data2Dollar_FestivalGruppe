import twint
import pandas as pd


def get_tweets():

    print("Fetching Tweets")
    c = twint.Config()
    # choose username
    c.Username = "realdonaldtrump"
    # choose beginning time
    c.Since = "2015-01-01 00:00:00"
    # customize table
    c.Custom['tweet'] = ["id", "date", "time", "timezone", "tweet", "link"]
    # format to csv
    c.Store_csv = True
    # name the csv file
    c.Output = "trumptweets_twint_v1.csv"
    twint.run.Search(c)


# run code
get_tweets()

# encode tweets with pandas
tweet_list = pd.read_csv('trumptweets_twint_v1.csv')
tweet_list.to_csv('trumptweets_twint.csv', index=False, encoding='utf-8-sig')
