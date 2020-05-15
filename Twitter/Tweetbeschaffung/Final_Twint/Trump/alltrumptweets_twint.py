import twint
import pandas as pd


def get_tweets():

    print("Fetching Tweets")
    c = twint.Config()
    # choose username
    c.Username = "realdonaldtrump"
    # choose beginning time
    c.Year = "2013"
    # customize table
    c.Custom['tweet'] = ["id", "date", "time", "timezone", "tweet", "link"]
    # format to csv
    c.Store_csv = True
    # name the csv file
    c.Output = "alltrumptweets_twint_uebergang.csv"
    twint.run.Search(c)


# run code
get_tweets()

# encode tweets with pandas
tweet_list = pd.read_csv('alltrumptweets_twint_uebergang.csv')
tweet_list.to_csv('alltrumptweets_twint.csv', index=False, encoding='utf-8-sig')
