print("*** Instagram Robot-Part1: ***")
print("***Approaches for Like the pages:****", "\n")

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

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

    
    def Search_Box(self, keyword):
        driver = self.driver
        
        # Click on the search icon
        try:
            search_icon = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[placeholder="Search"]'))
            )
            search_icon.click()
            time.sleep(20)
            search_icon.send_keys(keyword)  # Add the keyword
        except Exception as e:
            print("Search icon not clickable:", e)
        
        # Click on the first search result
        try:
            first_result = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.XPATH, '//div[@role="none"]/a'))
            )
            first_result.click()
        except Exception as e:
            print("First search result not found:", e)
        
        time.sleep(3)

    
    """**Approach1: Like function for ALL pages:***"""

    def LikeAllPosts(self):
        driver = self.driver
        time.sleep(2)

        # Open the first post if needed to start
        driver.find_element(By.CSS_SELECTOR, 'a[href="/curtain_hero/p/CW6nUtmq6pM/"]').click()
        time.sleep(3)

        last_height = driver.execute_script("return document.body.scrollHeight")

        while True:
            # Loop through posts on the current view and like if not already liked
            posts = driver.find_elements(By.XPATH, '//article//a')  # Adjust the selector to match posts
            for post in posts:
                post.click()  # Open post
                time.sleep(5)
                
                # Check if the post is already liked, avoid clicking "Unlike"
                like_button = driver.find_elements(By.XPATH, '//*[contains(@aria-label, "Like")]')
                unlike_button = driver.find_elements(By.XPATH, '//*[contains(@aria-label, "Unlike")]')
                
                if like_button and not unlike_button:
                    like_button[0].click()  # Click the like button if it exists and is not already liked
                    time.sleep(5)

                # Close the post
                driver.find_element(By.XPATH, '//button[contains(@aria-label, "Close")]').click()
                time.sleep(5)

            # Scroll down and load more posts
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)

            # Calculate new scroll height and compare to the last height
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                print("Reached the bottom, no more posts to load.")
                break  # Exit if no new posts are loaded
            last_height = new_height

        print("Finished liking all posts.")

    #################################################################################################################

    """**Approach2: Like function for 5 pages (our selection number pages):***"""
    # def Like(self):
    #     driver = self.driver
    #     time.sleep(2)

    #     # Open the first post
    #     driver.find_element(By.CSS_SELECTOR, 'a[href="/curtain_hero/p/CW6nUtmq6pM/"]').click()
    #     time.sleep(3)

    #     i = 1
    #     while i <= 5:
    #         time.sleep(2)
            
    #         # Check if the post is already liked (Avoid clicking "Unlike")
    #         if driver.find_elements(By.XPATH, '//*[contains(@aria-label, "Unlike")]'):
    #             time.sleep(3)
    #             # Move to the next post if already liked
    #             driver.find_element(By.LINK_TEXT, 'Next').click()
    #         elif driver.find_elements(By.XPATH, '//*[contains(@aria-label, "Like")]'):
    #             time.sleep(3)
    #             # Click "Like" button if it is available and not already liked
    #             # driver.find_element(By.CLASS_NAME, 'xp7jhwk').click()
    #             driver.find_element(By.XPATH, '//*[contains(@aria-label, "Like")]').click()
    #             time.sleep(3)
    #             driver.find_element(By.LINK_TEXT, 'Next').click()
            
    #         i += 1
        
    #     # Return to main page after finishing
    #     driver.find_element(By.CSS_SELECTOR, 'a[href="/curtain_hero/"]').click()
    #     print("Finished liking all posts.")

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
bot.Search_Box("curtain_hero") 

# for like all post:
bot.LikeAllPosts()
# for like 5 post:
# bot.Like()

bot.Logout
