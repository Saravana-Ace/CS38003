from bs4 import BeautifulSoup
import urllib.request

r = urllib.request.urlopen('https://www.cs.purdue.edu').read()

soup = BeautifulSoup(r)

# print out results
print(soup.prettify())
