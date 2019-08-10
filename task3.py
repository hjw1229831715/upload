from lxml import etree
import requests

url = 'https://www.xicidaili.com'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
}


def getIP():
    response = requests.get(url, headers=headers)
    text = response.text
    html = etree.HTML(text)
    # print(etree.tostring(html, encoding='utf-8').decode('utf-8'))

    # 使用xpath提取代理ip信息
    trs1 = html.xpath('//tr[@class="odd"]')
    trs2 = html.xpath('//tr[@class=""]')
    trs = trs1 + trs2
    ips = []
    for tr in trs:
        ip = tr.xpath('./td/text()')[0]
        http = tr.xpath('./td/text()')[4]
        port = tr.xpath('./td/text()')[1]
        if 'sock' in http:
            continue

        # ips.append(etree.tostring(http, encoding='utf-8').decode('utf-8').strip()+'://'+etree.tostring(ip,encoding='utf-8').decode('utf-8').strip())
        ips.append(http.lower() + '://' + ip + ':' + port)

    for ip in ips:
        print(ip)
        # print('\n')


if __name__ == "__main__":
    getIP()