# import requests
# import re
# from bs4 import BeautifulSoup
# from lxml import etree
#
# tags = ['小说']
#
# indexUrl = "https://book.douban.com/subject/4913064/"
#
# headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'}
# strurl = requests.get(indexUrl,headers=headers)
#
# # seletor = etree.HTML(strurl.text)
# # string = ''
# # li = seletor.xpath('//*[@id="info"]')
# # name = seletor.xpath('//*[@id="wrapper"]/h1/span')
# # name = name[0].text
# # print(name)
# # author = seletor.xpath('//*[@id="info"]/span[1]/a')
# # author = author[0].text
# # print(author)
# # public = seletor.xpath('//*[@id="info"]/text()')
# # for i in public:
# #     string = string + i
# # string = string.replace("\n","")
# # print(string)
# def get_request_res(pattern_text, html):
#     pattern = re.compile(pattern_text, re.S)
#     res = re.findall(pattern, html)
#     if len(res) > 0:
#         return res[0].split('<', 1)[0][1:]
#     else:
#         return 'NULL'
#
# def parse_one_page(html):
#     book_info = {}
#     book_name = get_bs_res('div > h1 > span', html)
#     book_info['Book_name'] = book_name
#     author = get_bs_res('div > span:nth-child(1) > a', html)
#     if author is None:
#         author = get_bs_res('#info > a:nth-child(2)', html)
#     author = author.replace(" ", "")
#     author = author.replace("\n", "")
#     book_info['Author'] = author
#
#     publisher = get_request_res(u'出版社:</span>(.*?)<br/>', html)
#     book_info['publisher'] = publisher
#
#     publish_time = get_request_res(u'出版年:</span>(.*?)<br/>', html)
#     book_info['publish_time'] = publish_time
#
#     ISBN = get_request_res(u'ISBN:</span>(.*?)<br/>', html)
#     book_info['ISBN'] = ISBN
#
#     author_intro = get_bs_res('#content > div > div.article > div.related_info > div:nth-child(4) > div > div > p', html)
#     book_info['author_intro'] = author_intro
#
#     grade = get_bs_res('div > div.rating_self.clearfix > strong', html)
#     if len(grade) == 1:
#         book_info['Score'] = 'NULL'
#     else:
#         book_info['Score'] = grade[1:]
#
#     comment_num = get_bs_res('#interest_sectl > div > div.rating_self.clearfix > div > div.rating_sum > span > a > span', html)
#     book_info['commments'] = comment_num
#
#     five_stars = get_bs_res('#interest_sectl > div > span:nth-child(5)', html)
#     book_info['5_stars'] = five_stars
#
#     four_stars = get_bs_res('#interest_sectl > div > span:nth-child(9)', html)
#     book_info['4_stars'] = four_stars
#
#     three_stars = get_bs_res('#interest_sectl > div > span:nth-child(13)', html)
#     book_info['3_stars'] = three_stars
#
#     two_stars = get_bs_res('#interest_sectl > div > span:nth-child(17)', html)
#     book_info['2_stars'] = two_stars
#
#     one_stars = get_bs_res('#interest_sectl > div > span:nth-child(21)', html)
#     book_info['1_stars'] = one_stars
#
#     return book_info
#
# def get_bs_res(selector, html):
#     soup = BeautifulSoup(html, 'lxml')
#     res = soup.select(selector)
#
#     if res is None:
#         return 'NULL'
#     elif len(res) == 0:
#         return 'NULL'
#     else:
#         return res[0].string
#
#
# info = parse_one_page(strurl.text)
# print(info)

headers = ['Book_name','Author','publisher','publish_time','ISBN','author_intro','Score','commments','5_stars','4_stars','3_stars','2_stars','1_stars']
info = [{'Book_name': '活着', 'Author': '余华', 'publisher': '作家出版社', 'publish_time': '2012-8-1', 'ISBN': '9787506365437', 'author_intro': 'NULL', 'Score': '9.4 ', 'commments': '500780', '5_stars': '75.4%', '4_stars': '22.2%', '3_stars': '2.2%', '2_stars': '0.1%', '1_stars': '0.1%'},
{'Book_name': '坏小孩', 'Author': '紫金陈', 'publisher': '湖南文艺出版社', 'publish_time': '2018-7-1', 'ISBN': '9787540468422', 'author_intro': 'NULL', 'Score': '7.4 ', 'commments': '47837', '5_stars': '19.7%', '4_stars': '45.0%', '3_stars': '29.5%', '2_stars': '4.6%', '1_stars': '1.3%'},
{'Book_name': '房思琪的初恋乐园', 'Author': '林奕含', 'publisher': '北京联合出版公司', 'publish_time': '2018-1', 'ISBN': '9787559614636', 'author_intro': 'NULL', 'Score': '9.2 ', 'commments': '194500', '5_stars': '67.6%', '4_stars': '27.7%', '3_stars': '4.2%', '2_stars': '0.3%', '1_stars': '0.2%'},
{'Book_name': '白夜行', 'Author': '[日]东野圭吾', 'publisher': '南海出版公司', 'publish_time': '2013-1-1', 'ISBN': '9787544258609', 'author_intro': 'NULL', 'Score': '9.1 ', 'commments': '275220', '5_stars': '68.9%', '4_stars': '26.6%', '3_stars': '4.1%', '2_stars': '0.3%', '1_stars': '0.2%'},
{'Book_name': '解忧杂货店', 'Author': '[日]东野圭吾', 'publisher': '南海出版公司', 'publish_time': '2014-5', 'ISBN': '9787544270878', 'author_intro': 'NULL', 'Score': '8.5 ', 'commments': '644034', '5_stars': '48.4%', '4_stars': '39.7%', '3_stars': '10.8%', '2_stars': '0.9%', '1_stars': '0.2%'},
{'Book_name': '追风筝的人', 'Author': '[美]卡勒德·胡赛尼', 'publisher': '上海人民出版社', 'publish_time': '2006-5', 'ISBN': '9787208061644', 'author_intro': 'NULL', 'Score': '8.9 ', 'commments': '649968', '5_stars': '57.2%', '4_stars': '35.6%', '3_stars': '6.6%', '2_stars': '0.4%', '1_stars': '0.2%'},
{'Book_name': '红楼梦', 'Author': '[清]曹雪芹著', 'publisher': '人民文学出版社', 'publish_time': '1996-12', 'ISBN': '9787020002207', 'author_intro': 'NULL', 'Score': '9.6 ', 'commments': '292768', '5_stars': '82.6%', '4_stars': '14.6%', '3_stars': '2.3%', '2_stars': '0.2%', '1_stars': '0.2%'}]

import csv

f = open('file.csv','w',encoding='utf-8')
csv_writer = csv.writer(f)
csv_writer = csv.DictWriter(f,headers)
csv_writer.writeheader()
for i in info:
    print(type(i))
    csv_writer.writerow(i)

f.close()
