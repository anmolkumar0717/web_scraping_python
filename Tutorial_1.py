from bs4 import BeautifulSoup

import requests 

url="https://boston.craigslist.org/search/sof"

response=requests.get(url)

data=response.text
# print(data)

soup=BeautifulSoup(data,'html.parser')
print(soup)

title_pages=soup.find_all("a",{"class":"result-title"})
addresses=soup.find_all("span",{"class":"result-hood"})
for title_page in title_pages:
	t=title_page.text
	print(t)

for adress in addresses:
	print(adress.text)



