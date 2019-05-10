from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os


class igBot:

    def __init__(self,username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome()

    def closeBrowser(self):
        self.driver.close()

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(2)
        userElem = driver.find_element_by_xpath("//input[@name='username']")
        userElem.send_keys(self.username)
        userElem.clear()
        passElem = driver.find_element_by_xpath("//input[@name='password']")
        passElem.send_keys(self.password)
        passElem.clear()
        passElem.send_keys(Keys.RETURN)
    
    def likePhoto(self, hastag):
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/" + hastag + "/")
        for i in range(1, 3):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)

        # searching link photo
        hrefs = driver.find_elements_by_tag_name("a")
        picHref = [elem.get_attribute("href") for elem in hrefs]
        # picHref = [href for href in picHref if hastag in href]
        print(hastag + "Photo : " + str(len(picHref)))
        # print(picHref)

        for hs in picHref:
            driver.get(hs)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            try:
                driver.find_elements_by_link_text("Like").click()
                print("liked")
                time.sleep(18)
            except Exception as e:
                print("tidak ditemukan")
                time.sleep(5)

        driver.close()

fadliIg = igBot("selaz.ioia@yahoo.com", "fadliselaz13")
fadliIg.login()
time.sleep(5)
fadliIg.likePhoto("prabowo")

# hastags = ["gowes", "bike", "sepedatouring"]
# [fadliIg.likePhoto(tag) for tag in hastags]