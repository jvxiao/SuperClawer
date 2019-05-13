import Spider
import requests
import json
import time
def getTitle():
	ti = []
	kv = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0"}
#url = 'https://www.toutiao.com/api/pc/realtime_news/'
	url='http://www.toutiao.com/api/pc/feed/?category=news_society'
	wbdata = requests.get(url, headers=kv).text
#	print(wbdata)
	data = json.loads(wbdata)
	news = data['data']

	for n in news:    
  		title = n['title']    
 # img_url = n['image_url']    
 # url = n['media_url']    
  	#	print(title)
		ti.append(title)
	return ti


def app2():
	old = []
	for i in range(50):
		title = getTitle()
		if(i==1):
			old = getTitle()
			for j in old:
				print(j)
		for til in title:
			if til not in old:
				old.append(til)
				print(til)
	for k in old:
		print(k)	

