from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome(executable_path="./chromedriver")
browser.get("https://www.twitter.com/")

time.sleep(3)
email = browser.find_element_by_name("session[username_or_email]")
email.send_keys("selaz.ioia@yahoo.com")
ps = browser.find_element_by_name("session[password]")
ps.send_keys("tigabelas1313", Keys.ENTER)


trend = """
#JanganCurangiSuaraRakyat
#225MeninggalPecatKetuaKPU
"""

source = requests.get("https://www.gelora.co/").text

soup = BeautifulSoup(source, "html5lib")

div = soup.find("div", class_="widget-content popular-posts")

for i in div.find_all("a"):
    msg = f"""
{i.text}
{trend}
{i["href"]}
"""
    twt = browser.find_element_by_id("tweet-box-home-timeline")
    twt.send_keys(msg)

    time.sleep(5)
    # twt.send_keys(Keys.CONTROL + Keys.RETURN)

    print(f"""
    ===================
    message terTWEET :
    ===================
    {i.text}
    {trend}
    {i["href"]}
    ===================
    """)
    
    time.sleep(300)
    # print(i.text)
    # print(" ")
    # print(i["href"])
    # print("\n===============\n")