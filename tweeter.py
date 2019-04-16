from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


# profile = webdriver.FirefoxProfile()
# profile.set_preference("network.proxy.type", 1)
# profile.set_preference("network.proxy.socks", "127.0.0.1")
# profile.set_preference("network.proxy.socks_port", 9150)

browser = webdriver.Chrome(executable_path="./chromedriver")
browser.get("https://www.twitter.com/")


email = browser.find_element_by_name("session[username_or_email]")
email.send_keys("selaz.ioia@yahoo.com")
ps = browser.find_element_by_name("session[password]")
ps.send_keys("tigabelas1313", Keys.ENTER)

time.sleep(10)

msg = """
Jangan Lupa Bangun Subuh besok,
dan langsung #GerakanSubuhAkbarIndonesia
"""
twt = browser.find_element_by_id("tweet-box-home-timeline")
twt.send_keys(msg)


time.sleep(5)
twt.send_keys(Keys.CONTROL + Keys.RETURN)

