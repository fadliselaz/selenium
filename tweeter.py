from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from pesan import *

browser = webdriver.Chrome(executable_path="./chromedriver")
browser.get("https://www.twitter.com/")

time.sleep(3)
email = browser.find_element_by_name("session[username_or_email]")
email.send_keys("selaz.ioia@yahoo.com")
ps = browser.find_element_by_name("session[password]")
ps.send_keys("tigabelas1313", Keys.ENTER)


msg = msgPoll

for i in msg:
    twt = browser.find_element_by_id("tweet-box-home-timeline")
    twt.send_keys(i)

    time.sleep(5)
    twt.send_keys(Keys.CONTROL + Keys.RETURN)

    print(f"""
    ===================
    message terTWEET :
    ===================
    {i}
    ===================
    """)
    
    time.sleep(300)

