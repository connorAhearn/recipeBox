# Web scraper design pattern from following links:
# https://realpython.com/beautiful-soup-web-scraper-python/
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/

import requests
from bs4 import BeautifulSoup
import bs4


URL = "https://www.sipandfeast.com/pasta-alla-norcina/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

# soup.stripped_strings is our "Content" to loop through
for string in soup.stripped_strings:
    print(string)

