import requests
from bs4 import BeautifulSoup


url = "https://www.skysports.com/premier-league-table"
r = requests.get(url)

# print source code site's text:
# print(r.text) # for exracting informatio you must use BeautifullSoup

soup = BeautifulSoup(r.text, "html.parser")
# print(soup)


print("\n" , "***Extract Table Data****   :", "\n")

# <div class="sdc-site-table__table-heading-wrapper"><h2 class="sdc-site-table__table-heading"><a class="sdc-site-table__table-heading-link" href=/premier-league>Premier League</a></h2>
table = soup.find("table")
# print(table)


# head & row html code:
# <thead class="sdc-site-table__head">
#   <tr class="sdc-site-table__row">
#     <th scope="col" class="sdc-site-table__cell" data-priority="1" data-push="" id="th--0">


print("approach2")
# Create an empty list to store the table headers

# Find all rows in the table
rows = table.select("tr")

headers = []

# Extract headers (assuming they're in the first row)
for head in rows[0].select('th'):
    headers.append(head.text.strip())
    print(headers)

# Process remaining rows (skip the header row)
for row in rows[1:]:
    data = []  # Create an empty list to store data for each row
    for cell in row.select('td'):
        data.append(cell.text.strip())
    print(data)    
    # Print the row data with headers for clarity
    for i, header in enumerate(headers):
        print(f"{header}: {data[i] if len(data) > i else ''}")  # Handle potential index out of range
    print()  # Add a newline between rows
