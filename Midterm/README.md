# WELCOME TO MIDTERM FOLDER

- This shall be a good place for you to find my midterm attempt for a basic natural language processing implementation :tada:
- I should keep the intro short, let's get it begin 

## :bookmark: Objectives
Crawl data from vnexpress (at least 5 topic, 40 documents/1 topic)

Output:  
-  Pre processing (stopword, html,tokenize…)
Extract TF-IDF feature
Using SVM for training of document classification
Evaluate by Accuracy

## :bookmark: Objective evaluation 
- [] Crawl data from Vnexpress from 5 topics, 40 articles/topic => 200 articles in total
- [] Data pre processing
- [] Extract model using TF-IDF feature
- [] Using SVM for training of document classification
- [] Evaluate by Accuracy



## :question: How I started? 
- Look, as a dummy in Machine Learning, I do read the books first and things that read are all in `Books` folder

## :question: Crawling data from a website - VnExpress

- Articles you can reach
    
    * [Best 3 Ways to Crawl Data from a Website](https://www.octoparse.com/blog/how-to-crawl-data-from-a-website)

- But look, I have some here :smile:

<p align = "center">
    <img src = "https://i.ibb.co/qM27wr0/image.png" width="250px"/>
</p>

- Okie, let's practice, let the game begin with crawling data manually from a simple article. Visit `Crawling_practice` for more
    - URL: https://e.vnexpress.net/news/news/first-saigon-metro-line-gets-power-4237364.html

- It's new to me so I will try to build myself a web crawler using Python

- We're gonna need a driver for your browser to make it work as a middleware. If you are using Chrome, [click here](http://jonathansoma.com/lede/foundations-2018/classes/selenium/selenium-windows-install/) for detailed installation

- Trying Scrapy from Python for website crawling lib

```
pip install scrapy
```

- But this requires Microsoft Visual C++ 14.0 or up so make sure you have it before the `pip`. But I don't recommend using `scrapy`

- Next, `Selenium`, still a scrawling tool but it does not require VS C++ or else just go ahead and 
```
pip install selenium
```