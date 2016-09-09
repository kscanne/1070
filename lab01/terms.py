from bs4 import BeautifulSoup
import requests

html = requests.get("https://en.wikipedia.org/wiki/Cosmology").text
soup = BeautifulSoup(html, 'html5lib')
