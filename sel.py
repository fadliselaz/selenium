from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


# profile = webdriver.FirefoxProfile()
# profile.set_preference("network.proxy.type", 1)
# profile.set_preference("network.proxy.socks", "127.0.0.1")
# profile.set_preference("network.proxy.socks_port", 9150)

browser = webdriver.Chrome(executable_path="./chromedriver")
browser.get("https://jatim.indeksnews.com/2019/02/03/polling-siapa-calon-anggota-dpr-ri-jawa-timur-dapil-xi-pilihan-anda/")


# email = driver.find_element_by_id("email")
# email.send_keys("selaz.ioia@yahoo.com")
# ps = driver.find_element_by_id("pass")
# ps.send_keys("selastio1307", Keys.ENTER)
