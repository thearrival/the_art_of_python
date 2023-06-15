import requests
from bs4 import BeautifulSoup


URL = raw_input("Input the website URL: ")
page = requests.get("https://" + URL)

info = page.text

soup = BeautifulSoup(info, "lxml")

for link in soup.find_all('a'):
      print(link.get('href'))
