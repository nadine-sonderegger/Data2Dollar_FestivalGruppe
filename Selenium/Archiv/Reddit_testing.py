from selenium import webdriver
from lxml import html
import time
import re
import csv

tweets = ["trump boeing", "trump walmart"]
tweets_result = dict()
#csv_file = 'AnzahlArtikel.csv'



for tweet in tweets:
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
    searchend_box.send_keys('08/16/2019')
    time.sleep(1)
    searchterm_box = driver.find_element_by_xpath('//*[@id="sterm"]')
    searchterm_box.send_keys(tweet)
    time.sleep(1)
    subreddit_box = driver.find_element_by_xpath('//*[@id="ssubreddits"]')
    subreddit_box.send_keys('wallstreetbets')
    time.sleep(1)
    execute_box = driver.find_element_by_xpath('//*[@id="execute-search"]')
    execute_box.click()
    time.sleep(3)

    number_of_posts = len(driver.find_elements_by_xpath("//div[contains(@class, 'submission')]"))
#    number_of_posts = len(driver.find_elements_by_xpath("//div[@id='results-container']/div[@id='post']//div[@class='submission']"))
    print(number_of_posts)
    print(type(number_of_posts))

    #AB HIER WERDEN DIE SUCHERGEBNISSE VON EINER SUCHER UNTERSUCHT

    #AB HIER UNTERSUCHUNG DER POSTS
    count_number_post = 0
    max_number_of_posts = 0
    allposts_comment_number = 0

    count_number_post = count_number_post + 1
    max_number_of_posts = len(driver.find_elements_by_xpath("//div[contains(@class, 'submission')]"))
    range_of_posts = list(range(count_number_post, max_number_of_posts+1))
    print(range_of_posts)

    for post in range_of_posts:
        post_box = driver.find_element_by_xpath('//*[@id="posts"]/div[{}]/div[1]/div[1]'.format(str(post)))
        post_comment_number = post_box.text
        allposts_comment_number = allposts_comment_number + int(post_comment_number)
        print(allposts_comment_number)

    #AB HIER UNTERSUCHUNG DER COMMENTS
    max_number_of_comments = 0
    min_number_of_comments = 0
    allcomments_likes_number = 0

    min_number_of_comments = min_number_of_comments + 1
    max_number_of_comments = len(driver.find_elements_by_xpath("//div[contains(@class, 'score') and not(@class='score-container')]"))
    range_of_comments = list(range(min_number_of_comments, max_number_of_comments+1))
    print(range_of_comments)
    print(max_number_of_comments)

    for comment in range_of_comments:
        comment_box = driver.find_element_by_xpath('//*[@id="comments"]/div[{}]/div/div[2]/div[2]'.format(str(comment)))
        comment_box_number = int(comment_box.text[:-7])
        print(comment_box_number)
        allcomments_likes_number = allcomments_likes_number + comment_box_number
        print(allcomments_likes_number)

    #Die Ergebnisse hinzufügen
    tweets_result[tweet] = [max_number_of_posts, allposts_comment_number, max_number_of_comments, allcomments_likes_number]

print(tweets_result)

    #print("Anzahl Posts: " + str(max_number_of_posts))
    #print("Anzahl Kommentare für alle Posts: " + str(allposts_comment_number))
    #print("Anzahl Kommentare: " + str(max_number_of_comments))
    #print("Anzahl Likes für alle Kommentare: " + str(allcomments_likes_number))
