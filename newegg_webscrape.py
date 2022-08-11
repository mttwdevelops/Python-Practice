from bs4 import BeautifulSoup
import requests
import re

search_term = input("What product are you looking for? ")
url = f"https://www.newegg.com/p/pl?d={search_term}&n=4841"

result = requests.get(url).text
doc = BeautifulSoup(result, "html.parser")

# checks num of pages if need to scrape any further
page_num = str(doc.find(class_="list-tool-pagination-text").strong)
total_num_pages = int(page_num.split(">")[3][0])

items_dict = {}

for page in range(1, total_num_pages + 1):
    url = f"https://www.newegg.com/p/pl?d=3070&n=4841&page={page}"
    page = requests.get(url).text
    doc = BeautifulSoup(page, "html.parser")

    div = doc.find(class_="item-cells-wrap border-cells items-grid-view four-cells expulsion-one-cell")
    items = div.find_all(text = re.compile(search_term))
    for item in items:
        parent = item.parent
        if parent.name != "a":
            continue
        link = parent["href"]
        next_parent = item.find_parent(class_ = "item-container")

        try:
            price = next_parent.find(class_ = "price-current").find("strong").string
            items_dict[item] = {"price" : int(price.replace(",", "")), "link": link}

        except:
            pass

# sort dict
sorted_items_dict = sorted(items_dict.items(), key=lambda x: (x[1]['price']))

for item in sorted_items_dict:
    print(item[0])
    print(f"${item[1]['price']}")
    print(f"{item[1]['link']}")
    print("------------------------")