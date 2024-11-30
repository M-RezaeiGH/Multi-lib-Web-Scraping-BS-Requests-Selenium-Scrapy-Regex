import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

print("***Meghdad IT: For buying laptops**** :", "\n")

url = "https://meghdadit.com/productlist/laptop/?page="

titles = []
stars = []
prices = []

for page in range(1, 3):  # range: 1 to 2 and does not include 3
    pages = requests.get(url + str(page))
    # print(pages.text)
    soup = BeautifulSoup(pages.text, "html.parser")
    # print(soup)

    # Printing product titles:
    title = soup.select("div.list-item-title")  # Use sharpe # to find elements other than class, such as "id": ("button#submit")
    # print(title)
    for t in title:
        # print(t.text)
        name = t.text
        titles.append(name)

    # If users provided ratings (similar to Digikala):
    # star = soup.select("div.text-body2-strong text-neutral-700")
    # for s in star:
    #     rate = s.text.strip()
    #     # print(rate)
    #     stars.append(rate)

    # Printing product prices:
    price = soup.select("div.list-price-wrapper")
    for p in price:
        pr = p.text.strip()
        # print(pr)
        prices.append(pr)


# To save data in Excel, we create a dictionary:
product = {"Title": titles, "Price": prices}  # We don't have "Star": stars

# Group dictionary values based on columns or dictionary keys:
data = pd.DataFrame.from_dict(product, orient="index")  # Orient specifies how the 2D structure of the DataFrame is converted to a 1D structure, like a list of dictionaries or a dictionary of lists.

# Formatting the data nicely:
data = data.transpose()

# Saving data:
print("Saving data with the new format:")
# Get the current directory path
# You can set a custom path or create a workspace in VS Code
current_directory = os.getcwd()
# Create file path
file_path = os.path.join(current_directory, "MeghdadIT_Price_List.xlsx")

# Save the data
with pd.ExcelWriter(file_path) as writer:
    data.to_excel(writer, index=False)  # 'index=False' prevents saving the index

print("Saving data with the old format:")
# writer = pd.ExcelWriter("MeghdadIT_Price_List.xlsx")
# # Convert writer to Excel file:
# data.to_excel(writer)
# writer.save()
