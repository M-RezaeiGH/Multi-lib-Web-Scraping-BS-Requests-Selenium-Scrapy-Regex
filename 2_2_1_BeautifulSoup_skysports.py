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

print("approach1: teachers approach")
# Find all rows in the table
rows = table.select("tr") # more powerfull than below code
# rows = table.find_all("tr")
# print(rows)
# print(type(rows))


for row in rows:
    data = []
    for head in row.find_all("th"):
        heads = head.text.strip().split('\n')[0] # clean headers output from 'Pl\nPlayed' to 'PI'
        # print(heads)
        data.append(heads)
    for body in row.find_all("td"):
        bodies = body.text.strip()
        # print(bodies)
        data.append(bodies)
    print(data)




