print("*** Instagram Robot-Part2: ***")
print("***Approaches for Comment and Follow:****", "\n")

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

print("***Commenting of 5 first post of juventus:****", "\n")

class Bot:
    def __init__(self, username, password):
        self.driver = webdriver.Chrome()
        self.username = username
        self.password = password
    
    def Login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/")
        
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username")))
        
        driver.find_element(By.NAME, "username").send_keys(self.username)
        driver.find_element(By.NAME, "password").send_keys(self.password)
        
        driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        time.sleep(5)

        # Click "Not Now" on the save login info popup, if it appears
        try:
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//div[text()="Not now"]'))).click()
        except Exception as e:
            print("Save Login Info popup did not appear:", e)

        time.sleep(5)

        # Click "Not Now" on the notifications popup, if it appears
        try:
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.HoLwm'))).click()
        except Exception as e:
            print("Notifications popup did not appear:", e)

    def comment(self):
        driver = self.driver
        driver.get('https://www.instagram.com/juventus/')
        # Choosing first right post:
        post = driver.find_element(By.CSS_SELECTOR, 'a[href="/juventus/reel/DB0qh0ntA5X/"]').click()
        i = 1
        while i <= 5 :
            time.sleep(5)
            waits = WebDriverWait(driver, 20)
            text = waits.until(EC.element_to_be_clickable(By.CLASS_NAME, 'x1ejq31n'))
            text.click()
            text = waits.until(EC.element_to_be_clickable(By.CLASS_NAME, 'x1ejq31n'))
            # وارد كردن عبارت مورد نظر و شبيه سازي و كليك دكمه پست
            text.send_keys('Hi Guys!'+ Keys.ENTER)
            time.sleep(5)
            next = driver.find_element(By.LINK_TEXT,'Next').click()
            i += 1
        driver.get('https://www.instagram.com/juventus/')
    
    def follower(self):
        driver = self.driver
        driver.get('https://www.instagram.com/juventus/')
        waits = WebDriverWait(driver, 20)
        flw = waits.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/juventus/followers/"]')))
        flw.click()
        # Loop to click the follow button for each person:

        # approach_1:Loop to click the follow button for each person using **Counter Loop**
        for i in range(1, 7):  # For each person from 1 to 6
            xpath = f'/html/body/div[6]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div[{i}]/div/div/div/div[3]/div/button'
            follow_button = driver.find_element(By.XPATH, xpath)
            follow_button.click()
            time.sleep(5)  # Wait between clicks
        
        # # approach_2: Loop to click the follow button for each person using **format function**
        # for i in range(1, 7):  # For each person from 1 to 6
        #     xpath = '/html/body/div[6]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div[{}]/div/div/div/div[3]/div/button'.format(i)
        #     follow_button = driver.find_element(By.XPATH, xpath)
        #     follow_button.click()
        #     time.sleep(5)  # Wait between clicks
        
        driver.get('https://www.instagram.com/juventus/')

    

    #################################################################################################################
    def Logout(self):
        driver = self.driver
        time.sleep(5)
        
        more_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//span[text()="More"]'))
        )
        more_button.click()
        time.sleep(5)

        logout_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//span[text()="Switch accounts"]'))
        )
        logout_button.click()
        time.sleep(5)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "username"))
        )

        driver.quit()
        print("Logged out successfully and closed the browser.")

########################################################################################################################

# Example usage
username = "your_username"
password = "your_password"
bot = Bot(username, password)
bot.Login()
# bot.Search_Box("example_keyword") #curtain_hero
bot.comment()
bot.follower()
bot.Logout










