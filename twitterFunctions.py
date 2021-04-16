import csv
import os.path
import re
import requests
import time

from bs4 import BeautifulSoup
from selenium import webdriver

def driverBuilder(url):
    driver = webdriver.Chrome('./chromedriver')
    driver.get(url)
    time.sleep(2)

    return driver


def requestBuilder(url):
    for i in range(5):
        response=requests.get(url,headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36', })
        if response:
            break
        else:
            time.sleep(2)

    if not response:
        return None
    else:
        return response


def parseUserData(response):
	

def tweet_scrape(tot_tweets=1000):

	return


def run(dataFilename='twitter_data.txt', rebuildTraining=True, setSize=10000, scrapeMore=False):
	alreadySeen = set()
	for i in range(setSize):
		#TODO URL
		response = requestBuilder(url)
		user_data = parseUserData(response.text)
		if user_names['at'] in alreadySeen:
			print('Already Seen user ' + user_names['at'])
			i = i-1
			continue
		alreadySeen.add(user_names['at'])


	return
