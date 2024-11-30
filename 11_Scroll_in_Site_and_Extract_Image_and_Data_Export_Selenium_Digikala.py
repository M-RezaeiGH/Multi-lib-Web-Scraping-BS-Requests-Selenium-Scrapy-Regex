print("*** Extracting Specific Images from Digikala with Automatic Scrolling and Pagination: ***", "\n")


print("***1-Approach1 for  Choosing page and automated Scrolling:****", "\n")


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import os
import requests
from urllib.parse import urljoin

# Get the number of pages to download from the user
max_page = int(input("Enter the number of pages to download images from: "))

# Base URL for leather and gold bracelet with placeholder for page number
base_url = "https://www.digikala.com/search/?page={}&q=%DA%86%D8%B1%D9%85%20%D9%88%20%D8%B7%D9%84%D8%A7"

# Initialize WebDriver
driver = webdriver.Chrome()

# Create a folder for saving images
folder_name = 'DigiBraceletJPEGImages'
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

jpeg_urls = []

# Function to collect images from the specified section on the current page
def collect_images_on_page():
    # Find the specific section containing the images: we choose just main images and not others
    section = driver.find_element(By.XPATH, '//*[@id="ProductListPagesWrapper"]/section[1]/div[2]')
    
    # Extract all picture elements within this section
    pictures = section.find_elements(By.TAG_NAME, 'picture')
    
    for picture in pictures:
        sources = picture.find_elements(By.TAG_NAME, 'source')
        for source in sources:
            # find images links with get attribute:
            img_url = source.get_attribute('srcset')
            # Check if the URL is for a JPEG image - we don't consider .webp format files
            if img_url and 'image/jpeg' in source.get_attribute('type'):
                # Ensure the URL is complete
                if img_url.startswith('/'):
                    img_url = urljoin(driver.current_url, img_url)
                jpeg_urls.append(img_url)
                break  # Only one JPEG URL per picture

# Function to scroll down to the bottom of the page to load more images
def scroll_to_bottom():
    # Get the initial height of the page
    last_height = driver.execute_script("return document.body.scrollHeight")
    
    while True:
        # Scroll down to the bottom of the page
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        # Wait for new content to load
        time.sleep(2)
        
        # Calculate new scroll height and compare with the last height
        new_height = driver.execute_script("return document.body.scrollHeight")
        
        if new_height == last_height:
            # If heights are the same, break the loop
            break
        last_height = new_height

# Loop through the specified number of pages
for page in range(1, max_page + 1):
    # Navigate to the page
    driver.get(base_url.format(page))
    time.sleep(5)  # Wait for the page to load

    # Close any pop-up that asks for notifications
    try:
        close_popup = driver.find_element(By.XPATH, "//button[contains(., 'فعلا نه')]")
        close_popup.click()
    except NoSuchElementException:
        pass  # If there's no pop-up, continue

    # Scroll to the bottom of the page to load all images
    scroll_to_bottom()

    # Collect images on the current page
    collect_images_on_page()

    print(f"Collected images from page {page}")

# Download and save JPEG images
for index, url in enumerate(jpeg_urls):
    try:
        # Download image
        response = requests.get(url)
        if response.status_code == 200:
            # Save image in folder
            image_path = os.path.join(folder_name, f'image_{index + 1}.jpg')
            with open(image_path, 'wb') as file:
                file.write(response.content)
            print(f'Saved: {image_path}')  # Print saved image path
        else:
            print(f'Failed to download image (status code {response.status_code}): {url}')
    except requests.exceptions.RequestException as e:
        print(f'Error downloading image {url}: {e}')
    except Exception as e:
        print(f'Unexpected error for image {url}: {e}')

# Close the driver
driver.quit()


######################################################################################

print("***2- Approach1 for just Automated Scrolling:****", "\n")

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.common.exceptions import NoSuchElementException
# import time
# import os
# import requests
# from urllib.parse import urljoin


# # URL for leather and gold bracelet
# url = "https://www.digikala.com/search/?q=%DA%86%D8%B1%D9%85%20%D9%88%20%D8%B7%D9%84%D8%A7"
# driver = webdriver.Chrome()
# driver.get(url)

# time.sleep(5)

# # Close any pop-up that asks for notifications
# try:
#     close_popup = driver.find_element(By.XPATH, "//button[contains(., 'فعلا نه')]")
#     close_popup.click()
# except NoSuchElementException:
#     print("No discount popup to close.")

# time.sleep(5)

# # Create a folder for saving images
# folder_name = 'DigiBraceletJPEGImages'
# if not os.path.exists(folder_name):
#     os.makedirs(folder_name)

# jpeg_urls = []

# # Function to collect images from the specified section on the current page
# def collect_images_on_page():
#     # Find the specific section containing the images
#     section = driver.find_element(By.XPATH, '//*[@id="ProductListPagesWrapper"]/section[1]/div[2]')
    
#     # Extract all picture elements within this section
#     pictures = section.find_elements(By.TAG_NAME, 'picture')
    
#     for picture in pictures:
#         sources = picture.find_elements(By.TAG_NAME, 'source')
#         for source in sources:
#             img_url = source.get_attribute('srcset')
#             # Check if the URL is for a JPEG image
#             if img_url and 'image/jpeg' in source.get_attribute('type'):
#                 # Ensure the URL is complete
#                 if img_url.startswith('/'):
#                     img_url = urljoin(driver.current_url, img_url)
#                 jpeg_urls.append(img_url)
#                 break  # Only one JPEG URL per picture

# # Function to scroll down to the bottom of the page to load more images
# def scroll_to_bottom():
#     # Get the initial height of the page
#     last_height = driver.execute_script("return document.body.scrollHeight")
    
#     while True:
#         # Scroll down to the bottom of the page
#         driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
#         # Wait for new content to load
#         time.sleep(2)
        
#         # Calculate new scroll height and compare with the last height
#         new_height = driver.execute_script("return document.body.scrollHeight")
        
#         if new_height == last_height:
#             # If heights are the same, break the loop
#             break
#         last_height = new_height

# # Loop through all pages
# while True:
#     # Scroll to the bottom of the page to load all images
#     scroll_to_bottom()
    
#     # Collect images on the current page
#     collect_images_on_page()

#     # Try to go to the next page
#     try:
#         next_button = driver.find_element(By.CSS_SELECTOR, "a[aria-label='صفحه بعد']")
#         next_button.click()
#         time.sleep(5)  # Wait for the next page to load
#     except NoSuchElementException:
#         print("No more pages left.")
#         break  # Exit loop if there's no next page

# # Download and save JPEG images
# for index, url in enumerate(jpeg_urls):
#     try:
#         # Download image
#         response = requests.get(url)
#         if response.status_code == 200:
#             # Save image in folder
#             image_path = os.path.join(folder_name, f'image_{index + 1}.jpg')
#             with open(image_path, 'wb') as file:
#                 file.write(response.content)
#             print(f'Saved: {image_path}')  # Print saved image path
#         else:
#             print(f'Failed to download image (status code {response.status_code}): {url}')
#     except requests.exceptions.RequestException as e:
#         print(f'Error downloading image {url}: {e}')
#     except Exception as e:
#         print(f'Unexpected error for image {url}: {e}')

# # Close the driver
# driver.quit()

