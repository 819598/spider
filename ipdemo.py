import requests
from lxml import etree
import redis

#从ip地址代理上获取免费ip代理
#并构建ip代理池
def getIpPool():
    indexUrl = 'https://www.kuaidaili.com/free/inha/'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'}

    ipport = []
    for i in range(1, 2, 1):
        url = indexUrl + '{}/'.format(i)
        indexData = requests.get(url, headers=headers)
        seletor = etree.HTML(indexData.text)
        for j in range(1, 16, 1):
            ip = seletor.xpath('//*[@id="list"]/table/tbody/tr[{}]/td[1]'.format(j))
            port = seletor.xpath('//*[@id="list"]/table/tbody/tr[{}]/td[2]'.format(j))
            ipport.append(ip[0].text + ':' + port[0].text)

    Url = 'https://www.baidu.com'
    m = 0
    for i in ipport:
        proxies = {"http": "http://" + str(i)}
        request = requests.get(Url, headers=headers, proxies=proxies)
        if request.status_code == 200:
            r = redis.StrictRedis(host='localhost',port=6379,decode_responses=True)
            r.set('{}'.format(m),i)
            print('插入成功')
        m += 1

#检查ip是否有效
#有效返回True
def checkIp(ip):
    Url = 'https://www.baidu.com'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'}
    proxies = {"http":"http://" + str(ip)}
    request = requests.get(Url, headers=headers, proxies=proxies)
    if request.status_code == 200:
        return True
    else:
        return False

