#URLOPEN is a python module that works to gather html file for any website 

from urllib.request import urlopen


# Now we are going to load the target website
html = urlopen(input(" Enter the website URL: "))
print("-"*60)
print(html.read())
