# -*- coding: UTF-8 -*-

from urllib import request
from lxml import etree
import re
import pymysql

# 数据库连接
def connect():
    conn = pymysql.connect(host='localhost',
                           port=3306,
                           user='root',
                           password='123456',
                           database='blog_data',
                           charset='utf8mb4')

    # 获取操作游标
    cursor = conn.cursor()
    return {"conn": conn, "cursor": cursor}

connection = connect()
conn, cursor = connection['conn'], connection['cursor']

sql_insert = "insert into spider_data(id, plantform, read_num, fans_num, rank_num, like_num, create_date) values (UUID(), %(plantform)s, %(read_num)s, %(fans_num)s, %(rank_num)s, %(like_num)s, now())"

# csdn

req_csdn = request.Request('https://blog.csdn.net/meteor_93')
req_csdn.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36')
html_csdn = request.urlopen(req_csdn).read().decode('utf-8')
read_num_csdn = etree.HTML(html_csdn).xpath('//*[@id="asideProfile"]/div[2]/dl[5]/@title')[0]
fans_num_csdn = etree.HTML(html_csdn).xpath('//*[@id="fanBox"]/@title')[0]
rank_num_csdn = etree.HTML(html_csdn).xpath('//*[@id="asideProfile"]/div[3]/dl[4]/@title')[0]
like_num_csdn = etree.HTML(html_csdn).xpath('//*[@id="asideProfile"]/div[2]/dl[3]/@title')[0]

csdn_data = {
    "plantform": 'csdn',
    "read_num": read_num_csdn,
    "fans_num": fans_num_csdn,
    "rank_num": rank_num_csdn,
    "like_num": like_num_csdn
}

cursor.execute(sql_insert, csdn_data)
conn.commit()

print("---------CSDN 数据写入完成---------")

# juejin

req_juejin = request.Request('https://juejin.im/user/5d1ff49c6fb9a07eb67db07b/posts')
req_juejin.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36')
html_juejin = request.urlopen(req_juejin).read().decode('utf-8')
read_num_juejin = etree.HTML(html_juejin).xpath('//*[@id="juejin"]/div[2]/main/div[3]/div[2]/div/div[1]/div[2]/div[2]/span/span/text()')[0].replace(",", "")
fans_num_juejin = etree.HTML(html_juejin).xpath('//*[@id="juejin"]/div[2]/main/div[3]/div[2]/div/div[2]/a[2]/div[2]/text()')[0].replace(",", "")
rank_num_juejin = etree.HTML(html_juejin).xpath('//*[@id="juejin"]/div[2]/main/div[3]/div[2]/div/div[1]/div[2]/div[3]/span/span/text()')[0].replace(",", "")
like_num_juejin = etree.HTML(html_juejin).xpath('//*[@id="juejin"]/div[2]/main/div[3]/div[2]/div/div[1]/div[2]/div[1]/span/span/text()')[0].replace(",", "")

juejin_data = {
    "plantform": 'juejin',
    "read_num": read_num_juejin,
    "fans_num": fans_num_juejin,
    "rank_num": rank_num_juejin,
    "like_num": like_num_juejin
}

cursor.execute(sql_insert, juejin_data)
conn.commit()

print("---------掘金 数据写入完成---------")