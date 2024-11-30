import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import re
import random
import os

# site for web scrapping:
url_image = "https://www.banimode.com/Brand/239" # چرم-مارال


print("***Download All Images from site:**** :", "\n")

def download_images(image_urls, folder_name="leader_images_bottegaveneta"):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    for idx, url in enumerate(image_urls):
        response = requests.get(url)
        if response.status_code == 200:
            image_path = os.path.join(folder_name, f"image_{idx + 1}.jpg")
            with open(image_path, 'wb') as file:
                file.write(response.content)
            print(f"Downloaded {image_path}")
        else:
            print(f"Failed to download image from {url}")

def download(base_url, total_pages): 
    """
    Function for download from more than one pages
    base_url is our image_urls
    pls write the number of total_pages
    """
    # creating images folder
    folder_name = "leader_images_bottegaveneta"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    for page in range(1, total_pages + 1):
        # Constructing the URL for each page
        url = f"{base_url}?page={page}"
        print(f"Downloading images from {url}...")

        r = requests.get(url)
        if r.status_code != 200:
            print(f"Failed to retrieve page {page}.")
            continue
        
        soup = BeautifulSoup(r.text, "html.parser")
        links_soup = soup.find_all("img", src=re.compile(".jpg"))

        # Extracting image URLs
        image_urls = [info.get('src') for info in links_soup]

        # Download images using the combined function
        download_images(image_urls, folder_name)

    print(f"Images downloaded in '{folder_name}' folder.")

total_pages = 1  # You can change this to any number of pages you want to download

download(url_image, total_pages)
















