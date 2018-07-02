# Tool_Python_web-spider
This tool is designed for crawling and saving websites in multiple threads.
The web-spider aims to crawl not only the whole websites, but also to crawl elements of websites, such as pictures and text.

## Motivation.
When training deep neural network, the most important part is collecting enough amount of data.
One of effecient resource of data is website, thus, it's important to collect neccessary data from website in effecient way.

## Usage.
***STEP1***
For using this web spider, you should firstly write all the configuration into config/spider.conf. 
The configuration in 'spider.conf' supported by now includes:

[spider]: Section Header. Eg. [spider]

url_list_file: The text file which contains the url seed for crawling. Eg. config/urls

output_directory: The output fold to save crawled HTML pages. Eg. ./output

max_depth: The maximum depth related to seed url for crawling. Eg. 2

crawl_interval: The sleep time between each crawling, in the unit of second, which is designed not to interupt websites' operation. Eg. 3

crawl_timeout: The maximum waiting time for http response, in the unit of second. Eg. 6

target_url: The Regular Expression to define the url format which should be downloaded. Eg. *.(htm|html)$

thread_count: The thread number set to crawl website, which is used to speed up crawling. Eg. 6

***STEP2***
Then run the following script:
    
    python mini_spider.py -c config/spider.conf
  
***Unit Test***
The method for unit test:
    
    python -m unittest mini_spider_test


## Version and Abilty
  - Version 0.1.0:  Fetching the websites.
  - Version Next:  Fetching the pictures.

