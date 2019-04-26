from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

# tanya trending yang digunakan
t1 = str(input("Pilih Trending Topic1 : \n"))
t2 = str(input("Pilih Trending Topic2: \n"))
os.system("clear")
print("Wait...")
trend = f"{t1}\n{t2}"

# Selenium Section
browser = webdriver.Chrome(executable_path="./chromedriver")
browser.get("https://www.twitter.com/")

time.sleep(3)
email = browser.find_element_by_name("session[username_or_email]")
email.send_keys("selaz.ioia@yahoo.com")
ps = browser.find_element_by_name("session[password]")
ps.send_keys("tigabelas1313", Keys.ENTER)


# Beautifull Soup Section
source = requests.get("https://www.gelora.co/").text
soup = BeautifulSoup(source, "html5lib")


for i in soup.find_all("h2", class_="post-title entry-title"):
 
    msg = f"""
{i.text}
{trend}
{i.a["href"]}
"""
    msg = msg.strip("\n")
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
    {i.a["href"]}
    ===================
    """)
    
    time.sleep(300)
    # print(i.text)
    # print(" ")
    # print(i["href"])
    # print("\n===============\n")