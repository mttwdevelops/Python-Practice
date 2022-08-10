from bs4 import BeautifulSoup
import requests
import re



url = f"https://coinmarketcap.com/" # CHANGE URL
result = requests.get(url).text
doc = BeautifulSoup(result, "html.parser")

# first thing is that I want to establish connection to newegg
#       find url to search tab by prompting user for specific item
# 
# second is to figure out how to extract item name, relevant info
# 
# third is to figure out how to get all items of pages (look for classes, need to convert types)
# 
# fourth is to create a dictionary for our items

# fifth is to check all pages in range + 1 (since not starting at 0)
#   for different pages, need to run url, result, doc again
#   get next class / div that we can use for re.complile(search_term)

# then we iterate through items to get links, prices, create dictionary in dictionary for for item specifics

# sort list

# print item dictioanry in order