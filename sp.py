#coding=utf-8
import os,urllib,re,time

def getHtml(url):
	page = urllib.urlopen(url)
	html = page.read()
	return html

#def sendmsg():

def match(html):
	cache=raw_input("Press [enter] key continue...")
	os.system("reset")
	rule=r'<p class="time">(.*)</p>'
	pa=re.compile(rule)
	MSGtime=re.findall(pa,html)
	for i in MSGtime:
		gtime=unicode(i,"gbk")
	Nowtime=time.strftime('%Y-%m-%d-%H-%M',time.localtime(time.time()))
	pa2=re.compile(r"[0-9]*")
	ma=re.findall(pa2,i)
	while '' in ma:
		ma.remove('')
	wnow=[]
	xnow=[]
	for i in ma:
		for x in i:
			wnow.append(x)
	str(Nowtime)
	for i in Nowtime:
		if i=="-":
			pass
		else:
			xnow.append(i)
	Baa=0
	for i in range(0,8):
		if wnow[i]==xnow[i]:
			Baa+=1
		if Baa ==8:
			SendMSG=str(gtime)+"\n---------"+str(Nowtime)
			print SendMSG
#			sendqqmail(SendMSG,False)
			
	
	



def spider():
	try:
		html = getHtml("http://pvp.qq.com/cp/a20161115tyf/page1.shtml")
		print unicode(html,"gbk")
		print "[+]Download Done!"
	except:
		print "[-]Download Error!"
		exit()
	match(html)

def sleepRule():
	for i in range(0,100):
		tiem.sleep(37)

def main():
	try:
		while 1:
			sleepRule()
			spider()
	except:
		main()


if __name__=="__main__":
	main()
