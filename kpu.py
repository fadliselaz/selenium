from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions() 
#Path to your chrome profile
options.add_argument("user-data-dir=Users/fadliselaz/Library/Application Support/Google/Chrome/Profile 1/Default") 

browser = webdriver.Chrome(executable_path="./chromedriver", chrome_options=options)


browser.get("https://facebook.com")
time.sleep(3)
browser.execute_script("window.open('http://artace.id')")

# soup = BeautifulSoup(browser.page_source, "lxml")
# alls = soup.find_all(text="prabowo")
# print(alls)
