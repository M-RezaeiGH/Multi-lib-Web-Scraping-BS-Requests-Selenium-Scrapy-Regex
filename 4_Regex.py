import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import os

SourceCode_Regex = "https://pythex.org/"

print("***Regex**** :", "\n")

# site for web scrapping:
url = "https://quotes.toscrape.com/"

r = requests.get(url)
# print(r.text) 

soup = BeautifulSoup(r.text, "html.parser")
# print(soup)



print("*1-find div and a tag with tags approach:", "\n")
# data1 = soup.findAll([ "a", "div" ])
# for d in data1:
#     print(d)

print("*2-find div and a tag with Regex approach:", "\n")

# pattern1 = "(^a|div)"
# data2 = soup.findAll(re.compile(pattern1))
# for d in data2:
#     print(d)


print("*3-find all box element in site with Regex approach:", "\n")

print("*3-1-find with tags approach:", "\n")
# data3 = soup.find_all("div", class_="quote")
# # data3 = soup.select("div.quote")

# for d in data3:
#     print(d.text)


print("*3-2-find with Regex approach:", "\n")
pattern2 = '(^quote)'
data3 = soup.find_all("div", re.compile(pattern2))

for d in data3:
    print(d.text)



