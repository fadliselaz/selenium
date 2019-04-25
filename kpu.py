from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
from bs4 import BeautifulSoup


browser = webdriver.Chrome(executable_path="./chromedriver")


browser.get("https://pemilu2019.kpu.go.id/#/ppwp/hitung-suara/")
time.sleep(10)


soup = BeautifulSoup(browser.page_source, "lxml")
alls = soup.find_all(text="prabowo")
print(alls)
