#init

import requests
from bs4 import BeautifulSoup

url = 'http://www.nytimes.com'
r = requests.get(url)
r_html = r.text
soup = BeautifulSoup(r_html, "lxml")
title = soup.findAll(class_="story-heading")

for item in title:
    try:
        print(item.text.strip())
    except:
        pass