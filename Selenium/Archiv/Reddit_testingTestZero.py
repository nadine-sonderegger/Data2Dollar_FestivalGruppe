from selenium import webdriver
from lxml import html
import time
import re
import csv
import pandas as pd


#tweets = ["trump boeing", "trump walmart", "trump pfizer"]
tweets_result = dict()
#csv_file = 'AnzahlArtikel.csv'
#startdate = '04/15/2019'
#enddate = '08/16/2019'
tweets_result = {'apple': ['12.12.2016', '14.12.2016', 155, 122], 'boeing': ['01.02.2016', '03.02.2016', 888, 145], 'javier': ['18.08.1933', '20.08.1993', 123, 178]}

#excel = pd.read_excel('FINAL_vader_twint_dowjones.xlsx', sheet_name="FinalTweets")
#list_of_links = excel['Link'].tolist()
#list_of_tweets = excel['Company'].tolist()
#list_of_startdates = excel['startdate'].tolist()
#list_of_enddates = excel['enddate'].tolist()

#for a,b,c,d in zip(list_of_links, list_of_tweets, list_of_startdates, list_of_enddates):
    #print(a + b + c + d)

#tweets_result = dict()

dataframe = pd.DataFrame.from_dict(tweets_result, orient='index', columns=['Startdatum', 'Enddatum', 'Zahl1', 'Zahl2'])
print(dataframe)
dataframe.to_excel("TestOutput.xlsx")
