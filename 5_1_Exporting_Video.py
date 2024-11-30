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
url_video = "https://video.varzesh3.com/video/357698"


print("***Download Video:**** :", "\n")

print("*Approach_1  for download all qualities:", "\n")

# download file with more than one quality

def download(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    links_soup = soup.find_all("a", href=re.compile(".mp4"))
    # print(links)
    for info in links_soup:
        links = info.get('href')
        # print(links)
        with r.get(links, stream=True) as file_download:
            with open('video_1.mp4', 'wb') as f:
                for video in file_download.iter_content(chunk_size=1024):
                    f.write(video)

download(url_video)

print("*Approach_1 for download with our choosen qualities:", "\n")
print("download file with more than one quality")


##############################################################################################
print("*Approach_2 for our coosen quality: example 360p", "\n")

def download(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    
    # Find the link only for 360p quality
    link_360 = None
    
    # Search for the link with 360p quality
    for item in soup.find_all("a", href=re.compile(".mp4")):
        quality_span = item.find("span", string=re.compile("360"))

        if quality_span:
            link_360 = item['href']
            break  # Stop the loop once the link is found
    
    if link_360:
        print("Video link with 360p quality found:", link_360)
        
        # Download the video
        with requests.get(link_360, stream=True) as file_download:
            with open('video_1.mp4', 'wb') as f:
                for chunk in file_download.iter_content(chunk_size=1024):
                    f.write(chunk)
        print("Download completed and saved as 'video_1.mp4'.")
    else:
        print("Video with 360p quality not found.")

# Assuming url_video is defined correctly
download(url_video)


