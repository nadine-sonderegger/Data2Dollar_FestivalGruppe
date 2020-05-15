import twint
import pandas as pd


def get_tweets():

    print("Fetching Tweets")
    c = twint.Config()
    # choose username
    c.Username = "ABack"
    # choose beginning time
    c.Year = "2020-05-10"
    # customize table
    c.Custom['tweet'] = ["id", "date", "time", "timezone", "tweet", "link"]
    # format to csv
    c.Store_csv = True
    # name the csv file
    c.Output = "backtweets_twint_uebergang.csv"
    twint.run.Search(c)


# run code
get_tweets()

# encode tweets with pandas
tweet_list = pd.read_csv('backtweets_twint_uebergang.csv')
tweet_list.to_csv('backtweets_twint.csv', index=False, encoding='utf-8-sig')
