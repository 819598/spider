import requests
from bs4 import BeautifulSoup
from lxml import etree
import re

#开始标签，以豆瓣读书的首页开始
#豆瓣上以tag来统计图书，每个图书都有其一个或多个图书
#例如在tag小说下就有很多图书
indexUrl = "https://book.douban.com/"

#该页面下包含所有标签
url = "https://book.douban.com/tag/?view=cloud"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'}

#获取所有热门的标签
def getTags(url):
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

#获取每个标签的中的页面
def getPages(name):
    url = indexUrl + 'tag/' + name
    return url

#获取页面中每个图书的链接
def getBookPage(url,number):
    urls = []
    for i in range(0,number,20):
        url = url + '?start={}&type=T'.format(i)
        print(url)
        strurl = requests.get(url, headers=headers)
        seletor = etree.HTML(strurl.text)
        for j in range(1, 21, 1):
            xpath = '//*[@id="subject_list"]/ul/li[{}]/div[2]/h2/a/@href'.format(j)
            urls.append(seletor.xpath(xpath))
            if(len(urls) >= number):
                break
    return urls

#对爬取的文本进行正则判定
def getRequestRes(pattern_text, html):
    pattern = re.compile(pattern_text, re.S)
    res = re.findall(pattern, html)
    if len(res) > 0:
        return res[0].split('<', 1)[0][1:]
    else:
        return 'NULL'

#获取图书页面的html代码
def getHtml(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'}
    strurl = requests.get(url, headers=headers)

    return strurl.text
#获取图书的信息
def getBookPageInformation(html):
    book_info = {}
    book_name = getBsRes('div > h1 > span', html)
    book_info['Book_name'] = book_name
    author = getBsRes('div > span:nth-child(1) > a', html)
    if author is None:
        author = getBsRes('#info > a:nth-child(2)', html)
    author = author.replace(" ", "")
    author = author.replace("\n", "")
    book_info['Author'] = author

    publisher = getRequestRes(u'出版社:</span>(.*?)<br/>', html)
    book_info['publisher'] = publisher

    publish_time = getRequestRes(u'出版年:</span>(.*?)<br/>', html)
    book_info['publish_time'] = publish_time

    ISBN = getRequestRes(u'ISBN:</span>(.*?)<br/>', html)
    book_info['ISBN'] = ISBN

    author_intro = getBsRes('#content > div > div.article > div.related_info > div:nth-child(4) > div > div > p', html)
    book_info['author_intro'] = author_intro

    grade = getBsRes('div > div.rating_self.clearfix > strong', html)
    if len(grade) == 1:
        book_info['Score'] = 'NULL'
    else:
        book_info['Score'] = grade[1:]

    comment_num = getBsRes('#interest_sectl > div > div.rating_self.clearfix > div > div.rating_sum > span > a > span', html)
    book_info['commments'] = comment_num

    five_stars = getBsRes('#interest_sectl > div > span:nth-child(5)', html)
    book_info['5_stars'] = five_stars

    four_stars = getBsRes('#interest_sectl > div > span:nth-child(9)', html)
    book_info['4_stars'] = four_stars

    three_stars = getBsRes('#interest_sectl > div > span:nth-child(13)', html)
    book_info['3_stars'] = three_stars

    two_stars = getBsRes('#interest_sectl > div > span:nth-child(17)', html)
    book_info['2_stars'] = two_stars

    one_stars = getBsRes('#interest_sectl > div > span:nth-child(21)', html)
    book_info['1_stars'] = one_stars

    return book_info

#对图书页面的信息使用bs4进行分割
def getBsRes(selector, html):
    soup = BeautifulSoup(html, 'lxml')
    res = soup.select(selector)

    if res is None:
        return 'NULL'
    elif len(res) == 0:
        return 'NULL'
    else:
        return res[0].string

if __name__ == '__main__':
    tags = getTags(url)
    bookUrl = []

    for i in tags:
        url = getPages(i)
        bookUrls = getBookPage(url,30)
        for j in bookUrls:
            bookUrl.append(j[0])
        if(len(bookUrl) >= 30):
            break
    # for i in bookUrl:
    #     BookUrl = str(i)
    #     html = getHtml(BookUrl)
    #     info = getBookPageInformation(html)
    print(bookUrl)