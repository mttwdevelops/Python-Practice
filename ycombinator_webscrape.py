# Created 7/19/2022

import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(res.text, 'html.parser')
# print(res)  # if value is 200, then everything is fine.
# print(res.text) # gives the html of the website
# print(soup.select('.score'))

links = soup.select('.titlelink') # gets the newstitles since the titles are under the 'titlelink' class
subtext = soup.select('.subtext') # gets the number of upvotes. 

# to grab more than just the first 30 posts:
res2 = requests.get('https://news.ycombinator.com/news?p=2')
soup2 = BeautifulSoup(res2.text, 'html.parser')
links2 = soup2.select('.titlelink') # gets the newstitles since the titles are under the 'titlelink' class
subtext2 = soup2.select('.subtext')
mega_links = links + links2
mega_subtext = subtext + subtext2

def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key = lambda k:k['votes'], reverse=True)

def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            # print(points)
            if points >= 100:
                hn.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hn)

# print(create_custom_hn(links, subtext))
pprint.pprint(create_custom_hn(mega_links, mega_subtext))
# create_custom_hn(links, subtext)