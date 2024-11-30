import requests
from bs4 import BeautifulSoup

url = "https://www.python.org/"
r = requests.get(url)

# print source code site's text:
# print(r.text) # for exracting informatio you must use BeautifullSoup


soup = BeautifulSoup(r.text, "html.parser")
print(soup)

show1 = soup.find("a") # first a tag
print(f"first a tag show: {show1}")

print("*"* 100)

show2 = soup.find_all("a")  # it's similar code: soup.findAll
print(f"All a tag show: {show2}")

for s in show2:
    print(f"show all links with a href: {s['href']}")



# methods Select: which is more powerfull than find & findALL:
show3 = soup.select_one("p") # same as to find
show4 = soup.select("p") # same as to findALL

#Example for select: FIND GO'S CLICK text OBJECT IN PYTHON SITE:
# find with class:
show5 = soup.select_one("button.search-button")  # use dot .

# use sharp for find with every thing other than class , such as "id"
show5 = soup.select_one("button#submit") # use sharp #

print(show5.text)
# strip spaces:
print(show5.text.strip())

# # Method Find: use cictionary {"attribute":"attribute's text"}
show6 = soup.find("button", {'id': 'submit'}) 
show6 = soup.find("button", {'id': 'submit', 'class': 'search-button'})
print(show6.text.strip())




