from bs4 import BeautifulSoup
import requests

url = "https://coinmarketcap.com/"
result = requests.get(url).text
doc = BeautifulSoup(result, "html.parser")

tbody = doc.tbody

trs = tbody.contents

# print(trs[0].next_sibling) # should return ETH's html

prices = {}

for tr in trs[:10]:
    name, price = tr.contents[2:4]
    # print(tr.contents)
    name = tr.contents[2].p.string # we pick index 2 since the other indexes give other info such as rank, price, etc.
    price = tr.contents[3].a.string
    print(f"{name} {price}")


# The way I pick the p and a classes is that I inspect the element of the html and look for the classes with the info I want.