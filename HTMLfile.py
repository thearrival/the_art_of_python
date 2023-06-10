from urllib.request import urlopen

html = urlopen(input(" Enter the website URL: "))
print("-"*60)
print(html.read())
