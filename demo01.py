import requests
from bs4 import BeautifulSoup
from lxml import etree

#开始标签，以豆瓣读书的首页开始
#豆瓣上以tag来统计图书，每个图书都有其一个或多个图书
#例如在tag小说下就有很多图书
indexUrl = "https://book.douban.com/"

#该页面下包含所有标签
url = "https://book.douban.com/tag/?view=cloud"

def getTags(url):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'}
    strurl = requests.get(url,headers=headers)

    #tag用来保存爬取的标签名
    tag = []
    selector = etree.HTML(strurl.text)

    li = selector.xpath('//*[@id="content"]/div/div[1]/div[2]/div/table/tbody/*')

    for i in li:
        for j in i:
            m = j.xpath('./a[1]')
            tag.append(m[0].text)
    return tag

def getPages(url):
    url = url + '?start={.}&type=T'.format()

def getBookPage():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'}
    strurl = requests.get(indexUrl, headers=headers)

    seletor = etree.HTML(strurl.text)

    urls = []
    for i in range(1, 21, 1):
        urls.append(seletor.xpath('//*[@id="subject_list"]/ul/li[1]/div[2]/h2/a/@href'))
    return urls
def getBookInformation(url):
    information = []
    return information
