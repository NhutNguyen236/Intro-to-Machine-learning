# This is a simple web scraper using selenium to get all news titles from any Vnexpress URL

from selenium import webdriver
import csv

# If you did not leave your web driver in Scripts of Python, it will never work until  you determine the path to it 
driver = webdriver.Chrome('D:/chromedriver_win32/chromedriver.exe')

driver.get("https://vnexpress.net/phap-luat")
headlines = driver.find_elements_by_class_name("title-news")

for headline in headlines:
    
    print(headline.text.strip())