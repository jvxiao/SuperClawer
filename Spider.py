#coding:UTF-8
from bs4 import BeautifulSoup 
import html.parser
import requests

kv = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0"}
def getLinks(url):
	links_pool = []
	html = requests.get(url,headers = kv, allow_redirects=False)
	if html.status_code==200:
		soup = BeautifulSoup(html.content, 'html.parser')
		#print(soup.prettify().encode('utf-8'))     # 编码问题
		for links in soup.find_all('a'):
			print(links.get('href'))
			#links_pool.append[links.get('href')]
	else:
		print("something wrong happend")
	

links=getLinks("https://baike.baidu.com/item/%E5%9F%BA%E9%87%91")
getLinks(links for link in links)
	