from selenium import webdriver
import time
import re
#Liste mit den Suchstrings

#Driver der das Resultat holt
driver = webdriver.Chrome(executable_path=r"C:\Users\MaelCorbat\Desktop\ChromeDriver\chromedriver_win32\chromedriver.exe")
driver.get('http://www.google.com')
search_box = driver.find_element_by_name('q')
search_box.send_keys('langenthal')
search_box.submit()
time.sleep(2)
newsbutton = driver.find_element_by_xpath('//*[@id="hdtb-msb-vis"]/div[4]/a')
newsbutton.click()
time.sleep(3)
result_stats = driver.find_element_by_xpath('//*[@id="result-stats"]').text
print(result_stats)
result_stats_digit = re.sub("[^0-9]", "", result_stats)
total_search_results = result_stats_digit[:-3]
print(total_search_results)






#https://www.google.com/search?q={0}&source)lnms&tbm=nws

#//*[@id="hdtb-msb-vis"]/div[2]/a
