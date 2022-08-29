import pandas as pd
import requests
from bs4 import BeautifulSoup

def get_data(url):
    r = requests.get(url)
    return r.text

htmldata = get_data("https://www.goodreturns.in/petrol-price.html")
soup = BeautifulSoup(htmldata, 'html.parser')
result = soup.find_all("div", class_="gold_silver_table")
print(result)

mydatastr = ''
result = []
for table in soup.find_all('tr'):
    mydatastr += table.get_text()
mydatastr = mydatastr[1:]
itemlist = mydatastr.split("\n\n")

for item in itemlist[:-5]:
    result.append(item.split("\n"))

print(result)

df = pd.DataFrame(result[:-8])
print(df)