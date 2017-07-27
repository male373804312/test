# -*- coding: UTF-8 -*-
import re
import os
import requests
from lxml import etree
from bs4 import BeautifulSoup
from selenium import webdriver
from meizitu_next import request
from datetime import datetime
import redis

class meizi():
    # headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
    # all_url = 'http://www.mzitu.com'
    # strta_html = requests.get(all_url, headers=headers)

    # print r.get('gou')


    # def all_url(self, url):
    def all_url(self):
        # # straa_html =request(self, url)
        # strta_html = request.get(url, 3)
        # html = etree.HTML(strta_html.text)
        # # print type(html)
        # result = etree.tostring(html)
        # resul = etree.fromstring(result).xpath('//li/a/@href')   #使用xpath 来解析HTML 未成功。。。。。。
        # res = resul[6:]
        # print res
        # print len(resul)
        def list_iter(name):
            r = redis.Redis(host='localhost', port=6379, db=0)
            list_cout = r.llen(name)
            for index in xrange(list_cout):
                yield r.lindex(name, index)

        # for a in res:
        for a in list_iter('foo_list1'):
            print(u'开始保存：', a)  ##加点提示不然太枯燥了
            path = str(a)[-5:]  ##我注意到有个标题带有 ？  这个符号Windows系统是不能创建文件夹的所以要替换掉
            self.mkdir(path)  ##调用mkdir函数创建文件夹！这儿path代表的是标题title哦！！！！！不要糊涂了哦！
            self.html(a)  ##调用html函数把href参数传递过去！href是啥还记的吧？ 就是套图的地址哦！！不要迷糊了哦！


            # html_txt = requests.get(a, headers=headers)
            # html_txt = self.request(a)
            # html_soup = BeautifulSoup(html_txt.text, 'lxml')
            # max_span = html_soup.find('div', class_='pagenavi').find_all('span')[-2].get_text()
            # for page in range(1, int(max_span)+1):
            #     page_url = a + '/' +str (page)
            #     image_html = requests.get(page_url, headers=headers)
            #     image_soup = BeautifulSoup(image_html.text, 'lxml')
            #     img_url = image_soup.find('div', class_='main-image').find('img')['src']
            #     print img_url


    def html(self, href):  ##这个函数是处理套图地址获得图片的页面地址
        html = request.get(href, 3)
        max_span = BeautifulSoup(html.text, 'lxml').find('div', class_='pagenavi').find_all('span')[-2].get_text()
        for page in range(1, int(max_span) + 1):
            page_url = href + '/' + str(page)
            self.img(page_url)  ##调用img函数


    def img(self, page_url):  ##这个函数处理图片页面地址获得图片的实际地址
        img_html = request.get(page_url, 3)
        img_url = BeautifulSoup(img_html.text, 'lxml').find('div', class_='main-image').find('img')['src']
        self.save(img_url)


    def save(self, img_url):  ##这个函数保存图片
        name = img_url[-9:-4]
        img = request.get(img_url, 3)
        f = open(name + '.jpg', 'ab')
        f.write(img.content)
        f.close()


    def mkdir(self, path):  ##这个函数创建文件夹
        path = path.strip()
        isExists = os.path.exists(os.path.join("D:\mzititu", path))
        if not isExists:
            print(u'建了一个名字叫做', path, u'的文件夹！')
            os.makedirs(os.path.join("D:\mzititu", path))
            os.chdir(os.path.join("D:\mzititu", path))  ##切换到目录
            return True
        else:
            print(u'名字叫做', path, u'的文件夹已经存在了！')
            return False




    # def request(self, url):  ##这个函数获取网页的response 然后返回
    #     headers = {
    #         'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
    #     content = requests.get(url, headers=headers)
    #     return content

Mzitu = meizi() ##实例化
Mzitu.all_url()
# Mzitu.all_url('http://www.mzitu.com/page/2/')


