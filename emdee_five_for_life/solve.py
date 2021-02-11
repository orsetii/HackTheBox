import hashlib
import requests
from bs4 import BeautifulSoup

url='http://209.97.184.58:30039/'

s=requests.Session()	
r =s.get(url)
if r.status_code == 200:
	soup =BeautifulSoup(r.content, "html.parser")
	fin=soup.find('h3')
	tex=fin.text

h=hashlib.md5()
h.update(tex.encode("utf-8"))
ha=h.hexdigest()

print(s.post(url,data={'hash':ha}).text)
