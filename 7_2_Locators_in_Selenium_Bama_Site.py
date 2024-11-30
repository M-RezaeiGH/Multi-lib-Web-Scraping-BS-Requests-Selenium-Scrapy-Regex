from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

print("***Locators_in_Selenium_Bama Site:****", "\n")

url = "https://bama.ir/"
driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()

# Create a WebDriverWait object with a maximum wait time of 10 seconds
wait = WebDriverWait(driver, 10)

try:
    # Find the "Car" element in the main menu and click on it
    car_menu = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'خودرو')]")))
    car_menu.click()

    # Find and click on "Buy Car" in the submenu
    buy_car_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/car']")))
    buy_car_link.click()

    # Find and click on the "Brand, Model" button
    brand_model_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='stepped-selection__toggler']")))
    brand_model_button.click()

    # Find the search field and enter text
    search_field = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='جستجوی برند و مدل']")))
    search_field.send_keys("تویوتا کرولا")  # Enter search text
    search_field.send_keys(Keys.RETURN)  # Press the Enter key

    # Define a list of options
    options = [
        "تویوتا کرولا 1.8 لیتر GLI",
        "تویوتا کرولا 1.8 لیتر XLI",
        "تویوتا کرولا 2.0 لیتر GLI",
        "تویوتا کرولا 2.0 لیتر XLI"
    ]

    # Iterate to find and click on each option
    for option in options:
        try:
            # Find the desired option
            item = wait.until(EC.element_to_be_clickable((By.XPATH, f"//span[contains(text(), '{option}')]")))
            item.click()
            # Short delay to observe the click before moving to the next option
            time.sleep(3)
        except Exception as e:
            print(f"Error clicking on option '{option}':", e)

    # Wait a few seconds for the new page to load
    time.sleep(10)

finally:
    # Close the browser
    driver.quit()
