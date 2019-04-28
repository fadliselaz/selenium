from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

print("""
==================
Trending Twitter
==================
script : Fadliselaz
""")

source = requests.get("https://trends24.in/indonesia/").text

soup = BeautifulSoup(source, "lxml")

ol = soup.find("ol", class_="trend-card__list")
a = ol.find_all()

h = 0
num = 1
grabTrend = []
for i in a:
    h += 1
    if h % 2:
        print("--------------------------------------------\n")
    else:
        print(int(num/2), i.text)
        tambah = i.text
        grabTrend.append(tambah)
    num += 1

print("==================================")


# tanya trending yang digunakan
t1 = int(input("Pilih Trending Topic1 : \n"))
t2 = int(input("Pilih Trending Topic2: \n"))

# tanya waktu per POST
t3 = int(input("jeda waktu/Post/Menit: "))
waktu = t3 * 60

os.system("clear")
print("Wait...")
trend = f"{grabTrend[t1 - 1]}\n{grabTrend[t2 - 1]}"

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

    # executror POST
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
    
    time.sleep(waktu)
    # print(i.text)
    # print(" ")
    # print(i["href"])
    # print("\n===============\n")