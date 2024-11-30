from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

print("***Locators_in_Selenium_Google Site_Enter Approach:**** :", "\n")

url = "https://google.com/"
# driver = webdriver.Firefox()
driver = webdriver.Chrome()
driver.get(url)
# driver.maximize_window()

# find search box:
google_searchbox = driver.find_element(By.NAME,"q")

#write our text for search in search box + find enter key and click:
google_searchbox.send_keys('python'+Keys.ENTER)

print("*** Enter elemenent Approach:**** :", "\n")




# "Chrome Extention CSS_Selector"
Chrome_Extention_CSS_Selector = ".cHaqb"
WelcomeText_click = driver.find_element(By.CSS_SELECTOR,Chrome_Extention_CSS_Selector)
time.sleep(5)
WelcomeText_click.click()

time.sleep(5)
driver.close()





