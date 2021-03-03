'''
This is a simple page scrape which can access using a generic url, I will try to build it to scrape
[] Title
[] Topic
[] Author
[] Date
[] Content
'''
from selenium import webdriver

# Write data to Excel file 
import xlwt
from xlwt import Workbook

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
    #print(headline.text.strip())
    title = headline.text.strip()
    if(len(title) == 0):
        continue
    else:
        sheet1.write(row, 0, str(title))
        row = row + 1

# Save excel file .... and hhhm this needs a specification, fosho
workbook.save('./Data/titles.xls')