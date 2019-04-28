from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

options = webdriver.ChromeOptions() 
#Path to your chrome profile
options.add_argument("user-data-dir=Users/fadliselaz/Library/Application Support/Google/Chrome/Profile 1/Default") 

browser = webdriver.Chrome(executable_path="./chromedriver")


browser.get("https://accounts.google.com/signin/v2/identifier?hl=id&passive=true&continue=https%3A%2F%2Fwww.google.com%2F&flowName=GlifWebSignIn&flowEntry=ServiceLogin")

time.sleep(3)
email = browser.find_element_by_xpath("//input[@name='identifier']")
email.send_keys("fadliselaz", Keys.ENTER)

time.sleep(20)
browser.execute_script("window.open('https://youtube.com')")



# email.send_keys("fadliselaz")
# # ps = browser.find_element_by_name("session[password]")
# # ps.send_keys("tigabelas1313", Keys.ENTER)