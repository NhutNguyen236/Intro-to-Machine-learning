'''
After hanging around the whole day with my scrape_page which is a scraper that will scrape
title, content, topic of the news. I came up with the idea of making it more automational

Gotta add that auto crawl topic later, this is gonna take time

Steps to perform: 
- Get all url using find_element_by_css selector from page
- driver get every url in for loop to access to page
- Use technique in page_scrape to get content, title and topic
- Done

This scraper is not on top of the world tho because it needs a static url to run so you have to change it time to time
'''

# Libs import
from selenium import webdriver 
import xlwt
from xlwt import Workbook
import time

# Define topic list here to crawl 

# If you did not leave your web driver in Scripts of Python, it will never work until  you determine the path to it 
driver = webdriver.Chrome('D:/chromedriver_win32/chromedriver.exe')

# Define url path
main_url = "".join(["https://vnexpress.net/phap-luat"])
# Get url path
driver.get(main_url)

# Write titles to excel file
workbook = Workbook()
title_style = xlwt.easyxf('font: bold 1') 
sheet1 = workbook.add_sheet('Sheet 1')

# Step 1: Get all urls
# First, I am getting a list of web-element which stands for news title
titles = driver.find_elements_by_css_selector("h3 a[href*='https://vnexpress.net']")

# Get urls from titles
url_array = []
for t in titles:
    url = t.get_attribute('href')
    url_array.append(url)

# Specify row as the point to kick start writing
row = 1

# Specify head row for each field
content_style = xlwt.easyxf('alignment: wrap True')
sheet1.write(0, 0, 'Title', title_style)
sheet1.write(0, 1, 'Content', title_style)
sheet1.write(0, 2, 'Topic', title_style)

for u in url_array:
    # Write the title in xls first 
    sheet1.write(row, 0, str(t))
    # Step 2: Now I can get url from the title above

    # Go to the url to scrape things
    driver.get(u)

    # now this is where the game begins, let's scrape all the contents and topics baby!!!
    # Frist is the content
    contents = driver.find_elements_by_class_name("Normal")
    content_array = []

    for p in contents:
        #print(headline.text.strip())
        content = str(p.text.strip())
        content_array.append(content)

    # Convert the the array into 1 line string
    content_str = "\n".join(str(index) for index in content_array)

    # Re-write the array in cell of excel
    sheet1.write(row, 1, content_str, content_style)

    # Second, it is for topics
    xpath = "/html/body/section[5 or 4 or 3]/div/div[2]/div[1]/ul/li/a"
    topic = driver.find_element_by_xpath(xpath)
    sheet1.write(row, 2, topic.text)

    # Now increase the row for something else
    row = row + 1
    time.sleep(3)

# Save excel file .... and hhhm this needs a specification, fosho
workbook.save('./Data/data_test.xls')