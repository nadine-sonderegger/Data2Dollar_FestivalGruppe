from selenium import webdriver
import time
import re
import csv
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

excel = pd.read_excel('FINAL_vader_twint_dowjones.xlsx', sheet_name="AllCompanyTweets")
list_of_links = excel['link'].tolist()
list_of_tweets = excel['lower_case'].tolist()
print(list_of_tweets)
news_impact = {}

for a, b in zip(list_of_links, list_of_tweets):
    #driver = webdriver.Chrome('C:/webdrivers/chromedriver.exe')
    driver = webdriver.Chrome('/Users/NSonderegger/Desktop/chromedriver')
    driver.get('http://www.google.com')
    # time.sleep(2)
    #search_box = driver.find_element_by_name('q')
    #search_box = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')))
    search_box = WebDriverWait(driver, 20).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')))
    search_box.send_keys(b)
    time.sleep(2)
    search_box.submit()
    #search_button = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]')))
    # search_button.click()
    # time.sleep(5)
    #newsbutton = driver.find_element_by_link_text('News')
    newsbutton = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.LINK_TEXT, 'News'))).click()
    #newsbutton = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.link_text, 'News' )))
    # newsbutton.click()
    # time.sleep(2)
    #result_stats_box = driver.find_element_by_xpath('//*[@id="result-stats"]').text
    try:
        result_stats_box = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="result-stats"]')))
        result_stats = result_stats_box.text
        # print(result_stats)
        result_stats_digit = re.sub("[^0-9]", "", result_stats)
        total_search_results = result_stats_digit[:-3]
        news_impact[a] = [b, total_search_results]
        print(b + " " + total_search_results)
    except:
        news_impact[a] = [b, 0]

print(news_impact)

dataframe = pd.DataFrame.from_dict(news_impact, orient='index', columns=['Tweet', 'Anzahl Artikel'])
print(dataframe)
dataframe.to_excel("ResultsGoogleCrawl_AllTweets.xlsx")
# with open(csv_file, 'w') as csvfile:
#    csv_columns = ['Tweet', "Anzahl Artikel"]
#    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
#    for data in news_impact:

# https://stackoverflow.com/questions/28110008/python-selenium-wait-until-element-is-clickable-not-working

# //*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]
