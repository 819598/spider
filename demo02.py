import requests
import re
from bs4 import BeautifulSoup
from lxml import etree

tags = ['小说']

indexUrl = "https://book.douban.com/subject/4913064/"

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'}
strurl = requests.get(indexUrl,headers=headers)

# seletor = etree.HTML(strurl.text)
# string = ''
# li = seletor.xpath('//*[@id="info"]')
# name = seletor.xpath('//*[@id="wrapper"]/h1/span')
# name = name[0].text
# print(name)
# author = seletor.xpath('//*[@id="info"]/span[1]/a')
# author = author[0].text
# print(author)
# public = seletor.xpath('//*[@id="info"]/text()')
# for i in public:
#     string = string + i
# string = string.replace("\n","")
# print(string)
def get_request_res(pattern_text, html):
    pattern = re.compile(pattern_text, re.S)
    res = re.findall(pattern, html)
    if len(res) > 0:
        return res[0].split('<', 1)[0][1:]
    else:
        return 'NULL'

def parse_one_page(html):
    book_info = {}
    book_name = get_bs_res('div > h1 > span', html)
    book_info['Book_name'] = book_name
    author = get_bs_res('div > span:nth-child(1) > a', html)
    if author is None:
        author = get_bs_res('#info > a:nth-child(2)', html)
    author = author.replace(" ", "")
    author = author.replace("\n", "")
    book_info['Author'] = author

    publisher = get_request_res(u'出版社:</span>(.*?)<br/>', html)
    book_info['publisher'] = publisher

    publish_time = get_request_res(u'出版年:</span>(.*?)<br/>', html)
    book_info['publish_time'] = publish_time

    ISBN = get_request_res(u'ISBN:</span>(.*?)<br/>', html)
    book_info['ISBN'] = ISBN

    author_intro = get_bs_res('#content > div > div.article > div.related_info > div:nth-child(4) > div > div > p', html)
    book_info['author_intro'] = author_intro

    grade = get_bs_res('div > div.rating_self.clearfix > strong', html)
    if len(grade) == 1:
        book_info['Score'] = 'NULL'
    else:
        book_info['Score'] = grade[1:]

    comment_num = get_bs_res('#interest_sectl > div > div.rating_self.clearfix > div > div.rating_sum > span > a > span', html)
    book_info['commments'] = comment_num

    five_stars = get_bs_res('#interest_sectl > div > span:nth-child(5)', html)
    book_info['5_stars'] = five_stars

    four_stars = get_bs_res('#interest_sectl > div > span:nth-child(9)', html)
    book_info['4_stars'] = four_stars

    three_stars = get_bs_res('#interest_sectl > div > span:nth-child(13)', html)
    book_info['3_stars'] = three_stars

    two_stars = get_bs_res('#interest_sectl > div > span:nth-child(17)', html)
    book_info['2_stars'] = two_stars

    one_stars = get_bs_res('#interest_sectl > div > span:nth-child(21)', html)
    book_info['1_stars'] = one_stars

    return book_info

def get_bs_res(selector, html):
    soup = BeautifulSoup(html, 'lxml')
    res = soup.select(selector)

    if res is None:
        return 'NULL'
    elif len(res) == 0:
        return 'NULL'
    else:
        return res[0].string


info = parse_one_page(strurl.text)
print(info)