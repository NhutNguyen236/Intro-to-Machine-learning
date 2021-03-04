'''
    try_scraper is a testing module to get href from a simple css_selector 
    So can you scrape href from a class_name -> Yes, you can but in my case, NO.
'''

from selenium import webdriver
import csv

driver = webdriver.Chrome('D:/chromedriver_win32/chromedriver.exe')

driver.get("https://vnexpress.net/phap-luat")
headlines = driver.find_elements_by_css_selector("h3 a[href*='https://vnexpress.net']")


for headline in headlines:
    headline.click()
    drive
    print('click')