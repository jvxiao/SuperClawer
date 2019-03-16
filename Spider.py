#coding:UTF-8
from bs4 import BeautifulSoup 
import html.parser
import requests

def getLinks(url):
	links_pool = []
	html = requests.get(url)
	if html.status_code==200:
		soup = BeautifulSoup(html.content, 'html.parser')
		#print(soup.prettify().encode('utf-8'))     # 编码问题
		for links in soup.find_all('a'):
			print(links.get('href'))
			links_pool.append[links.get('href')]
	else:
		print("something wrong happend")
	

getSoup("https://www.baidu.com")
	