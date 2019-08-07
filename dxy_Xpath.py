#-*- coding:utf-8 -*-
#from contextlib import closing
import requests,json,re,os,sys,random,time
#from urllib.request import urlopen
#import urllib
from lxml import etree

class getUrl(object):
    """docstring for getUrl"""
    def __init__(self):
        self.headers={
            "Connection":"keep-alive",
            "User-Agent":"Mozilla/5.0 (Window NT 10.0; WOW64) AppleWebkit/537.36"
                         "(KHTML, like Gecko) Chrome/51.0.2704.63 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, sdch",
            "Accept-Language": "zh-CN,zh;q=0.8"
        };
    def run(self):
        url = "http://www.dxy.cn/bbs/thread/626626#626626"
        req=requests.get(url,headers=self.headers)
        html=req.text
        tree=etree.HTML(html)
        user=tree.xpath('//div[@class="auth"]/a/text()')
        content = tree.xpath('//td[@class="postbody"]')

        result=[]
        for i in range(0,len(user)):

            print(user[i].strip()+":"+content[i].xpath('string()').strip())   #.strip()用来去除首位空格
            print('*'*80)
if __name__=='__main__':
    geturl=getUrl()
    geturl.run()