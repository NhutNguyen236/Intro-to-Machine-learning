'''
After hanging around the whole day with my scrape_page which is a scraper that will scrape
title, content, topic of the news. I came up with the idea of making it more automational

Gotta add that auto crawl topic later, this is gonna take time
'''

# Libs import
from selenium import webdriver 
import xlwt
from xlwt import Workbook

# Define topic list here to crawl 

# If you did not leave your web driver in Scripts of Python, it will never work until  you determine the path to it 
driver = webdriver.Chrome('D:/chromedriver_win32/chromedriver.exe')

# Define url path
url = "".join(["https://vnexpress.net/phap-luat"])
# Get url path
driver.get(url)

headlines = driver.find_elements_by_class_name("title-news")

# Write titles to excel file
workbook = Workbook()
title_style = xlwt.easyxf('font: bold 1') 
sheet1 = workbook.add_sheet('Sheet 1')

# Specify row as the point to kick start writing
row = 1
# Specify title as head row
sheet1.write(0, 0, 'Title', title_style)

for headline in headlines:
    # Check out if the length of the title is 0 so continue to the next object
    title = headline.text.strip()
    if(len(title) == 0):
        continue
    else:
        sheet1.write(row, 0, str(title))
        # Magic begins from here, let's get some data
        
        row = row + 1

# Save excel file .... and hhhm this needs a specification, fosho
workbook.save('./Data/data_test.xls')