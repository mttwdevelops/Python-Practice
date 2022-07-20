# Created 7/19/2022

import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/news')
# print(res)  # if value is 200, then everything is fine.
# print(res.text) # gives the html of the website
soup = BeautifulSoup(res.text, 'html.parser')
# print(soup.select('.score'))

links = soup.select('.storylink') # gets the newstitles since the titles are under the 'storylink' class
subtext = soup.select('.subtext') # gets the number of upvotes. 

# Since the two above provide a list of all the different entries, we can use [0] to get the first index.

def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            print(points)
        hn.append({'title': title, 'link': href})
    return hn

# print(create_custom_hn(links, votes))
# print(links)
create_custom_hn(links, subtext)