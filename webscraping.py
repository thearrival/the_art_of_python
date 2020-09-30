import requests
from bs4 import BeautifulSoup


URL = str(input("Input the website URL: "))
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
