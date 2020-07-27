import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/known_by_Adegbolahan.html"
link_line = int(18) - 1
#relative to first link
count = int(7)

html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

while count >= 0:
   html = urllib.request.urlopen(url, context=ctx).read()
   soup = BeautifulSoup(html, 'html.parser')
   tags = soup('a')
   print(url)
   url = tags[link_line].get("href", None)
   count = count - 1