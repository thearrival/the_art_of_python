# URLOPEN is a python module that works to gather html file for any website.

from urllib.request import urlopen


# assign html to urlopen module
html = urlopen(input(" Enter the website URL: "))
print("-"*60)
print(html.read())
