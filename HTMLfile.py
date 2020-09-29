from urllib.request import urlopen

html = urlopen("input URL of the target")
print(html.read())
