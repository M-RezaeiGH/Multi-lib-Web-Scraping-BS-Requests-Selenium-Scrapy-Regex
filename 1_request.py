import requests

url = "https://www.python.org/"
response  = requests.get(url)
print(response)
print(response.request)
print(response.request.headers)

# Status code messages: 2 or 200:correct , first is 3 : transfer to another address , 4 or 404:wrong inalong side of users, 5: wrong along side of server
print(response.status_code)
print(response.reason)

print(response.headers)
###########################################

# print source code site's text:
print(response.text) # for exracting informatio you must use BeautifullSoup

###########################################
# download image python:
import requests

url1 = "https://www.python.org/static/img/python-logo@2x.png"

# Fetch the image content from the URL
response1 = requests.get(url1)

# Check for successful download
if response1.status_code == 200:
    with open('2.jpg', 'wb') as f:
        f.write(response1.content)
    print("Image downloaded successfully!")
else:
    print(f"Error downloading image: {response1.status_code}")

