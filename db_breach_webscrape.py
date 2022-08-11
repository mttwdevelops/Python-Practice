# File created 8/11/2022
# Source of data: https://en.wikipedia.org/wiki/List_of_data_breaches

from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://en.wikipedia.org/wiki/List_of_data_breaches"
result = requests.get(url).text
doc = BeautifulSoup(result, "html.parser")

leaks_table = doc.find("table", {"class": "wikitable"})
df = pd.read_html(str(leaks_table))
df = pd.DataFrame(df[0])

# Proof that it works:
# print(df.head())

df.to_csv("./databreachleaks.csv")