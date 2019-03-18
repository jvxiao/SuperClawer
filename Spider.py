#coding:UTF-8
from bs4 import BeautifulSoup 
#import html.parser
import requests

kv = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0"}
def getSoup(url):
#	links_pool = []
	html = requests.get(url,headers = kv, allow_redirects=False)
	if html.status_code==200:
		soup = BeautifulSoup(html.content, 'lxml')
		return soup
		print(soup.prettify().encode('utf-8'))     # 编码问题
	else:
		print("Something wrong!")	


def getLinks(soup):
	links_pool = []	
	for links in soup.find_all('a', target="_blank"):
		if links.string!=None and links!=None:
			print(links.string+"\t"+links.get('href'))
#			links_pool.append[links.string+links.get('href')]
	else:
		print("something wrong happend")
	

def getContent(soup):
	contents=soup.find_all(class_="para")
	for content in contents:
		if content!=None:
			print(content.string)
#	print(contents.encode("gbk"))
soup = getSoup("https://baike.baidu.com/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB/5162711?fr=aladdin")
#contents=getContent(soup)
#print(contents.encode("utf-8"))
getLinks(soup)
	
