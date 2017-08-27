# init
# this is a comment
import requests
from bs4 import BeautifulSoup

url = 'http://www.nytimes.com'  # defines what website to scrap
r = requests.get(url) # creates a var "holding" the request
r_html = r.text  # creates a var to which is written the result of the request
soup = BeautifulSoup(r_html, "lxml")
title = soup.findAll(class_="story-heading")

for item in title:
    try:
        print(item.text.strip())
    except:
        pass