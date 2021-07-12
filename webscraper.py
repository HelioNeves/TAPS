# HOW RUN IT:
# python3 webscraper.py [db-title] [urls-file]
# Data Wrangling packages
import sys
import numpy as np
import pandas as pd

# Webscraper packages
import scrapy
from scrapy.crawler import CrawlerProcess
from scraper.webscraper import IndeedSpider as Spider

def scraper(title, url_file):
    """A simple function that starts the webscraper.

        Iterates through the URL file acquiring the respective data. 

        Parameters
        ----------
        title : str
            The name of output database in .csv format
        url_file : str
            The location where the url file is located
    """
    print("\n>Scraper initalizing...\n")
    
    url = []
    for line in open(url_file, "r").readlines():
        url.append(line.strip())

    process = CrawlerProcess({"FEED_FORMAT": "csv", "FEED_URI": "db/" + title})
    process.crawl(Spider, start_urls=url)
    process.start()
    
    print("\n>Scraper done!")

scraper(sys.argv[1] + ".csv", sys.argv[2])
