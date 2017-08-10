# -*- coding: UTF-8 -*-
import requests
import re
import MySQLdb
from lxml import etree
def main_spider():
    #创建mysql数据库链接
    conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='373804312',
        db='world',
        # use_unicode=True,
        # charset="utf8"
    )
    conn.set_character_set('utf8')
    # 创建游标
    cur = conn.cursor()
    cur.execute("SET NAMES utf8")
    cur.execute("SET CHARACTER_SET_CLIENT=utf8")
    cur.execute("SET CHARACTER_SET_RESULTS=utf8")
    conn.commit()
    #创建数据库
    # cur.execute("create table Lianjia_database(Title VARCHAR (50),PLACE varchar(20),pattern varchar(10),AREA varchar(10), Subway VARCHAR (30), Price VARCHAR (8))")


    for num in range(1,100):
        rul = "https://bj.lianjia.com/ditiezufang/pg" + str(num) +'/'
        start_html = requests.get(rul)
        stata_list = re.findall(r'html" title="(.*?)">.*?</a></h2>(.*?)</li>', start_html.text, re.S)
        for i in stata_list:

            main_stat = re.findall(r'<span class="region">(.*?)&nbsp.*?"zone"><span>(.*?)&nbsp.*?class="meters">(.*?)&nbsp.*?class="fang-subway-ex"><span>(.*?)</span>.*?<span class="num">(.*?)</span>', i[1], re.S)

            for a in main_stat:
                print i[0]
                print a[0], a[1], a[2], a[3], a[4]
                print type(a[4])
                try:
                    sql = "insert into Lianjia_database values ('%s', '%s','%s','%s','%s','%s')" % (i[0], a[0], a[1], a[2], a[3], a[4])
                    cur.execute(sql)
                    conn.commit()
                except TypeError , e:
                    print e
                    print "输出失败"

    cur.close()
    conn.commit()
    conn.close()
main_spider()
