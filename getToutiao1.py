import Spider
import requests
import json
import time
import sim
def getTitle():
#	kv = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0"}
	kv = {
        'Host': 'www.toutiao.com',
        'User-Agent': 'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1; 125LA; .NET CLR 2.0.50727; .NET CLR 3.0.04506.648; .NET CLR 3.5.21022)',
        'Connection': 'Keep-Alive',
        'Content-Type': 'text/plain; Charset=UTF-8',
        'Accept': '*/*',
        'Accept-Language': 'zh-cn',
        'cookie':'__tasessionId=8q3as8o461554348325401'}
#url = 'https://www.toutiao.com/api/pc/realtime_news/'
#	url='http://www.toutiao.com/api/pc/feed/?category=news_society&utm_source=toutiao&widen=1&max_behot_time=0&max_behot_time_tmp=0&tadrequire=true'
	url=sim.get_new_url()
	wbdata = requests.get(url, headers=kv).text
#	print(wbdata)
	data = json.loads(wbdata)
	news = data['data']

	for n in news:    
  		title = n['title']    
 # img_url = n['image_url']    
 # url = n['media_url']    
  		print(title)

for i in range(10):
	getTitle()
	time.sleep(3)

