#coding: UTF-8
import Spider
import getToutiao
while(True):
	print("1. requests+BeautifulSoup爬取简书静态页面")
	print("2. requests+ API查找爬取JS动态网页")
	choice = raw_input("输入你的选择[1/2]:")
	if choice=='1':
		Spider.app1()
	elif choice=='2':
		getToutiao.app2()
	else:
		print("无效选择，退出.....")
		exit(0)
