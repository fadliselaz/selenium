from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os



userName = ["mtid7","mtid8","mtid9","mtid10","mtid11"]

for i in userName :
    browser = webdriver.Chrome(executable_path="./chromedriver")
    browser.get("https://www.vpnjantit.com/create-free-account.html?server=SG1&type=OpenVPN")
    time.sleep(2)
    browser.find_element_by_name("user").send_keys(i)
    browser.find_element_by_name("pass").send_keys(i)
    browser.find_element_by_name("pass").send_keys(Keys.ENTER)
    time.sleep(5)
    browser.quit()
    print(f"user dibuat : {i}")



