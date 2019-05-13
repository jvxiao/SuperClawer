#coding:UTF-8
import time
import hashlib 
url = 'https://www.toutiao.com/api/pc/feed/?category=news_hot&utm_source=toutiao&widen=1&max_behot_time=0&max_behot_time_tmp=0&tadrequire=true&'
def get_as_cp():
    zz ={}
    now = round(time.time())
    print now  #获取计算机时间
    e = hex(int(now)).upper()[2:]  #hex()转换一个整数对象为十六进制的字符串表示
    print e 
    i = hashlib.md5(str(int(now))).hexdigest().upper() #hashlib.md5().hexdigest()创建hash对象并返回16进制结果
    if len(e)!=8:
        zz = {'as': "479BB4B7254C150",
            'cp': "7E0AC8874BB0985"}
        return zz
    n=i[:5]
    a=i[-5:]
    r = ""
    s = ""
    for i in range(5):
        s = s+n[i]+e[i]
    for j in range(5):
        r = r+e[j+3]+a[j]
    zz = {
            'az': "A1" + s + e[-3:],
            'cp': e[0:3] + r + "E1"
        } 
    return zz
    print zz
def get_new_url():
	zz=get_as_cp()
	newurl = url+"as="+zz['az']+"&cp="+zz['cp']
	return newurl
	print(newurl)
