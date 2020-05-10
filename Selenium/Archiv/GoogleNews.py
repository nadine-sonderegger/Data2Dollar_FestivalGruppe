from selenium import webdriver
import time
import re
import csv

tweets= ["mael", "raoul", "nadine", "lorena"]
news_impact = {}

csv_file = 'AnzahlArtikel.csv'



for tweet in tweets:
    driver = webdriver.Chrome(executable_path=r"C:\Users\MaelCorbat\Desktop\ChromeDriver\chromedriver_win32\chromedriver.exe")
    driver.get('http://www.google.com')
    search_box = driver.find_element_by_name('q')
    search_box.send_keys(tweet)
    search_box.submit()
    #time.sleep(2)
    newsbutton = driver.find_element_by_link_text('News')
    newsbutton.click()
    #time.sleep(3)
    result_stats = driver.find_element_by_xpath('//*[@id="result-stats"]').text
    #print(result_stats)
    result_stats_digit = re.sub("[^0-9]", "", result_stats)
    total_search_results = result_stats_digit[:-3]
    news_impact[tweet] = total_search_results
    print(tweet + " " + total_search_results)

print(news_impact)

#with open(csv_file, 'w') as csvfile:
#    csv_columns = ['Tweet', "Anzahl Artikel"]
#    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
#    for data in news_impact:
#        writer.writerow(data)

#saving it to a string
#tweets_news = {}
#tweets_news[]

//*[@id="hdtb-msb-vis"]/div[5]/a


#https://www.google.com/search?q={0}&source)lnms&tbm=nws

#//*[@id="hdtb-msb-vis"]/div[2]/a

#//*[@id="hdtb-msb-vis"]/div[5]/a

#//*[@id="hdtb-msb-vis"]/div[2]/a

#//*[@id="hdtb-msb-vis"]/div[5]/a/span

#//*[@id="hdtb-msb-vis"]/div[5]/a/span/svg/path

#/html/body/div[6]/div[3]/div[3]/div/div/div[1]/div/div/div[1]/div/div[5]/a/span/svg/path
