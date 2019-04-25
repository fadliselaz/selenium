from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from pesan import msgPoll

browser = webdriver.Chrome(executable_path="./chromedriver")
browser.get("https://www.youtube.com/watch?v=lKg4DMEK0Rg")

signIn = browser.find_element_by_id("background")
signIn.click()
ip = browser.find_element_by_id("input")
ip.send_keys("Prabowo Sandi Untuk Indonesia..")


ip.send_keys(Keys.RETURN)

# msg = msgPoll

# for i in msg:
#     twt = browser.find_element_by_id("tweet-box-home-timeline")
#     twt.send_keys(i)


#     time.sleep(5)
#     print(f"""
#     ===================
#     message terTWEET :
#     ===================
#     {i}
#     ===================
#     """)
#     if i == 6:
#         break
#     time.sleep(300)

