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
		return soup, url
		print(soup.prettify().encode('utf-8'))     # 编码问题
	else:
		print("Something wrong!")	


def getLinks(soup,url):
	links_pool = []	
	for links in soup.find_all('a', class_="title"):
		if links.string!=None and links!=None:
			print(links.string+"\t"+url+links.get('href'))
#			links_pool.append[links.string+links.get('href')]
	else:
		print("something wrong happend")
	

def getContent(soup):   # 此处对应百度词条规则，不调用请忽略
	contents=soup.find_all(class_="para")
	for content in contents:
		if content!=None:
			print(content.string)
#	print(contents.encode("gbk"))

def app1():
	url = "https://www.jianshu.com/"
	soup,_ = getSoup(url)
	getLinks(soup, url)
#print(soup.prettify())
#contents=getContent(soup)
#print(contents.encode("utf-8"))
#getLinks(soup)
	
