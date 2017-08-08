# -*- coding: UTF-8 -*-
import redis
# import requests
from lxml import etree
from meizitu_next import request
r = redis.Redis(host='localhost', port=6379, db=0)
# r.set('goug', 'sahgn')
# r.set('gouh', 'sahgn')
# print r.get('gou')
# print r.get('gouh')
# r.rpush("foo_list1", 'gouh', 'gou', 'gou')
# for i in r.lrange("foo_list1",0,-1):   #遍历list
    # print r.rpop("foo_list1")
headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
all_url = 'http://www.mzitu.com/page/'
# strta_html = requests.get(all_url, headers=headers)
def Yeild(nist):
    for i in nist:
        yield i
for i in range(1, 147):
    start_html = request.get((all_url + str(i) + '/'), 3)
    html = etree.HTML(start_html.text)
    # print type(html)
    result = etree.tostring(html)
    resul = etree.fromstring(result).xpath('//li/a/@href')  # 使用xpath 来解析HTML 成功。。。。。。
    res = resul[6:]
    # print res
    # print len(resul)
    for n in Yeild(res):
        print n
        r.rpush("foo_list3", n)






