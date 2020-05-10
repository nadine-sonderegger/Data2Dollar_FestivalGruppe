from selenium import webdriver
import time
import re
import csv

tweets= ["mael", "raoul", "nadine", "lorena"]
news_impact = dict()
suche = ["trump boeing"]
#csv_file = 'AnzahlArtikel.csv'



for tweet in suche:
    driver = webdriver.Chrome(executable_path=r"C:\Users\MaelCorbat\Desktop\ChromeDriver\chromedriver_win32\chromedriver.exe")
    driver.get('https://redditsearch.io/')
    time.sleep(1)
    comment_box = driver.find_element_by_xpath('//*[@id="searchtype-selection"]/div/label[2]')
    comment_box.click()
    time.sleep(1)
    time_box = driver.find_element_by_xpath('//*[@id="time-selection"]/div/label[6]/span')
    time_box.click()
    time.sleep(1)
    searchstart_box = driver.find_element_by_xpath('//*[@id="sstart"]')
    searchstart_box.send_keys('04/15/2019')
    time.sleep(1)
    searchend_box = driver.find_element_by_xpath('//*[@id="send"]')
    searchend_box.send_keys('04/16/2019')
    time.sleep(1)
    searchterm_box = driver.find_element_by_xpath('//*[@id="sterm"]')
    searchterm_box.send_keys(tweet)
    time.sleep(1)
    subreddit_box = driver.find_element_by_xpath('//*[@id="ssubreddits"]')
    subreddit_box.send_keys('wallstreetbets')
    time.sleep(1)
    execute_box = driver.find_element_by_xpath('//*[@id="execute-search"]')
    execute_box.click()
    time.sleep(1)

    
    count_number_post = 0
    max_number_of_posts = 0

    try:
        post_box = driver.find_element_by_xpath('//*[@id="posts"]/div[1]/div[1]/div[1]')
        count_number_post = count_number_post + 1
        max_number_of_posts = len(driver.find_elements_by_xpath("//div[contains(@class, 'submission')]"))
        range_of_posts = (count_number_post, max_number_of_posts+1)

        for post in range_of_posts:
            post_box = driver.find_element_by_xpath('//*[@id="posts"]/div['+post+']/div[1]/div[1]')
            post_comment_number = post_box.text





    except:
        count_number_post = 0

    if count_number_post = 1:
        print (count_number_post)

    else:
        #loop nur mit comments


    post_box = driver.find_element_by_xpath('//*[@id="posts"]/div[1]/div[1]/div[1]')
    if not post_box:
        count_number_post = 0
        #count comments?
    else:
        count_number_post = 1
        post_comment_number = 0



        post = driver.find_element_by_xpath('//*[@id="posts"]/div['+count_number_post+']/div[1]/div[1]')
        #for info in post:
            post_comment_number = info.extract()
            po

            count_number_post = count_number_post + 1


#posts: Anzahl div Klassen submission zählen
len(driver.find_elements_by_xpath('//a'))
//*[@id="posts"]
//*[@id="posts"]/div[1]/div[1]/div[1]
//*[@id="posts"]/div[2]/div[1]

while self.driver.find_elements_by_xpath('//*[@title="Weiter"]‘):
sel = Selector(text=self.driver.page_source)
single_etikette = sel.xpath('//*[@class="listing-summary col-xs-12 col-sm-6"]‘)
for etikette in single_etikette:
unternehmens_name = etikette.xpath('.//*[@itemprop="name"]/text()').extract()
unternehmens_adresse = etikette.xpath('.//*[@class="address"]/text()').extract_first()
yield {'Name': unternehmens_name,
'Adresse': unternehmens_adresse}
element = self.driver.find_element_by_id('below-content')
self.driver.execute_script("arguments[0].scrollIntoView(0, document.documentElement.scrollHeight-5);", element)
sel = Selector(text=self.driver.page_source)
sleep(3)
self.driver.find_element_by_xpath('//*[@title="Weiter"]').click()


    #search_box.send_keys(suche)
    #search_box.submit()
    #time.sleep(2)
    #newsbutton = driver.find_element_by_link_text('News')
    #newsbutton.click()
    #time.sleep(3)
    #result_stats = driver.find_element_by_xpath('//*[@id="result-stats"]').text
    #print(result_stats)
    #result_stats_digit = re.sub("[^0-9]", "", result_stats)
    #total_search_results = result_stats_digit[:-3]
    #news_impact[tweet] = total_search_results
    #print(tweet + " " + total_search_results)

#print(news_impact)

#falls mehr als 10 ups --> crawl den inhalt des kommentars
