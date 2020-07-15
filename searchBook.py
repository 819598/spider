import requests
from lxml import etree

#豆瓣读书的网页
Url = 'https://book.douban.com/subject/10554308/comments/hot?p=1'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'}


def getComments(Url):
    start = time.time()
    #打开文件，准备数据写入
    f = open('comments.txt', 'w', encoding='utf-8')

    for i in range(1, 5, 1):
        url = Url + 'comments/hot?p={}'.format(i)
        for j in range(1, 21, 1):
            var = '//*[@id="comments"]/ul/li[{}]/div[2]/p/*'.format(j)
            commentData = requests.get(url, headers=headers)

            comments = etree.HTML(commentData.text)
            try:
                data = comments.xpath(var)
                f.writelines(data[0].text)
            except:
                print('ERROR')
            else:
                print(data[0].text)
    end = time.time()
    spendTime = end - start
    print(spendTime)
    f.close()


from wordcloud import WordCloud
import matplotlib.pyplot as plt
import jieba
import time

def makeWord():
    with open('comments.txt','r',encoding='utf-8') as f:
        text = f.read()
    cut_text = " ".join(jieba.cut(text))

    word = WordCloud(
        font_path = 'STXINWEI.TTF',
        background_color = 'white',

        max_words = 50,

        max_font_size = 60
    )
    wordcloud = word.generate(cut_text)
    wordcloud.to_file('cloud.jpg')
    plt.imshow(wordcloud,interpolation = 'bilinear')
    plt.axis("off")
    plt.show()

# url = 'https://book.douban.com/subject/1008145/'
# getComments(url)
makeWord()