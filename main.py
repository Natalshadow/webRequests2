# init
# this is a comment
import requests
from bs4 import BeautifulSoup
import openpyxl
wb = openpyxl.load_workbook('example.xlsx')
type(wb)

def webscrapper():
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


import openpyxl
wb = openpyxl.load_workbook('example.xlsx')
sheet = wb.get_sheet_by_name('Sheet1')
sheet['A1']

print(sheet['A1'].value)

c = sheet['B1']
print(c.value)

print('Row ' + str(c.row) + ', Column ' + c.column + ' is ' + c.value)

print('Cell ' + c.coordinate + ' is ' + c.value)

print(sheet['C1'].value)
