#-*- coding:utf-8 -*-
import urllib.request
from bs4 import BeautifulSoup as bs
def main():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)"
                          "Chrome/75.0.3770.142 Safari/537.36"
    }
    url='http://www.dxy.cn/bbs/thread/626626'
    request=urllib.request.Request(url,headers=headers)
    response = urllib.request.urlopen(request).read().decode("utf-8")
    html = bs(response, 'lxml')
    getItem(html)
def getItem(html):
    datas = []
    for data in html.find_all("tbody"):
        try:
            userid = data.find("div", class_="auth").get_text(strip=True)
            print(userid)
            content = data.find("td", class_="postbody").get_text(strip=True)
            print(content)
            datas.append((userid, content))
        except:
            pass
    print(datas)

if __name__ == '__main__':
    main()