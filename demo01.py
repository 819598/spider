import requests
from bs4 import BeautifulSoup
from lxml import etree
#//*[@id="content"]/div/div[1]/div[2]/div[1]

url = "https://book.douban.com/tag/?view=type&icn=index-sorttags-all"
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'}
strurl = requests.get(url,headers=headers)
print(strurl.text)
