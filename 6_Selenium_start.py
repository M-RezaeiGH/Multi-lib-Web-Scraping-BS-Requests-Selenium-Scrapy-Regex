import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time

print("***Selenium Library-start:**** :", "\n")
"https://7learn.com/blog/what-is-selenium"

# site for web scrapping:
url1 = "https://www.varzesh3.com/album"
url2 = "https://www.digikala.com/main/electronic-devices/"

driver = webdriver.Firefox()
# driver = webdriver.Chrome()

# open two url:
driver.get(url1)
driver.maximize_window()
time.sleep(5)
driver.get(url2)

# backward to url1
driver.back()

time.sleep(5)

# forward to url2
driver.forward()

# close webdriver
driver.close()






