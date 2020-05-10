from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path=r"C:\Users\MaelCorbat\Desktop\ChromeDriver\chromedriver_win32\chromedriver.exe")
driver.get('http://www.google.com')
search_box = driver.find_element_by_name('q')
search_box.send_keys('Bern')
search_box.submit()
time.sleep(5)
result_stats = driver.find_element_by_xpath('//*[@id="result-stats"]').text
print(result_stats)
