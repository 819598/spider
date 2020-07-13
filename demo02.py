import requests
from bs4 import BeautifulSoup
from lxml import etree

tags = ['小说']

indexUrl = "https://book.douban.com/subject/4913064/"

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'}
strurl = requests.get(indexUrl,headers=headers)

seletor = etree.HTML(strurl.text)
string = ''
li = seletor.xpath('//*[@id="info"]')
name = seletor.xpath('//*[@id="wrapper"]/h1/span')
name = name[0].text
print(name)
author = seletor.xpath('//*[@id="info"]/span[1]/a')
author = author[0].text
print(author)
public = seletor.xpath('//*[@id="info"]/text()')
for i in public:
    string = string + i
string = string.replace("\n","")
print(string)

def parse_one_page(html):
    book

    book_intro = get_bs_res('#link-report > div:nth-child(1) > div > p', html)
    book_info['book_intro'] = book_intro

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
    '''
    Get the book info by bs4 module
    :param selector: info selector
    :param html: page's html text
    :return: book's info
    '''
    soup = BeautifulSoup(html, 'lxml')
    res = soup.select(selector)
    # if res is not None or len(res) is not 0:
    #     return res[0].string
    # else:
    #     return 'NULL'
    if res is None:
        return 'NULL'
    elif len(res) == 0:
        return 'NULL'
    else:
        return res[0].string