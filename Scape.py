# Created 7/19/2022

import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/')
# print(res)  # if value is 200, then everything is fine.
# print(res.text) # gives the html of the website
soup = BeautifulSoup(res.text, 'html.parser')
print(soup.select('.score'))