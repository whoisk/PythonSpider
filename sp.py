#coding=utf-8
import urllib,re

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def FindInfo():
    html = getHtml("http://pvp.qq.com/cp/a20161115tyf/page1.shtml")
    print html
    print unicode(html,"gbk")

def main():
    FindInfo()


if __name__=="__main__":
    main()
