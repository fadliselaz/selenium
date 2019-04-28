# kali ini kita akan belajar untuk
# membuka tab baru dalam selenium,
# dan switch to ke tab baru tersebut

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions() 
#Path to your chrome profile
options.add_argument("user-data-dir=Users/fadliselaz/Library/Application Support/Google/Chrome/Profile 1/Default") 

browser = webdriver.Chrome(executable_path="./chromedriver", chrome_options=options)


browser.get("https://www.twitter.com/")

time.sleep(3)
email = browser.find_element_by_name("session[username_or_email]")
email.send_keys("selaz.ioia@yahoo.com")
ps = browser.find_element_by_name("session[password]")
ps.send_keys("tigabelas1313", Keys.ENTER)

time.sleep(5)

# script ini akan buka tab baru di browser
# mengikuti cookie yang sebelumnya login
# Tidak perlu login lagi
browser.execute_script("window.open('https://twitter.com/UmarGani20')")
