import requests
from lxml import etree
import time

#//*[@id="list"]/table/tbody/tr[1]/td[1]
indexUrl = 'https://www.kuaidaili.com/free/inha/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'}

ipport = []
for i in range(1,2,1):
    url = indexUrl + '{}/'.format(i)
    indexData = requests.get(url,headers=headers)
    seletor = etree.HTML(indexData.text)
    for j in range(1,16,1):
        ip = seletor.xpath('//*[@id="list"]/table/tbody/tr[{}]/td[1]'.format(j))
        port = seletor.xpath('//*[@id="list"]/table/tbody/tr[{}]/td[2]'.format(j))
        # print(ip[0].text)
        # print(port[0].text)
        ipport.append(ip[0].text + ':' + port[0].text)

Url = 'https://www.baidu.com'

for i in ipport:
    proxies = {"http": "http://" + str(ipport)}
    request = requests.get(Url, headers=headers, proxies=proxies)
    if request.status_code == 200:
        print('可用代理' + i)
    else:
        print('不可用代理' + i)