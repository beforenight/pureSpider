#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests


def get_yingyongbao_download_number():
    html_content = requests.get("http://sj.qq.com/myapp/detail.htm?apkName=net.shandian.app").content
    # 解析网页标签
    soup = BeautifulSoup(html_content, "html.parser")
    # 通过类名查找
    result = soup.select('.det-ins-num')
    # 获取下载数量信息 eg：119下载
    contents = result[0].contents.pop()
    # 分割字符串得到下载数量
    yingyongbao_numbers = contents[:len(contents) - 2]
    print "应用宝下载：\t", yingyongbao_numbers
    # 返回下载数量信息
    return yingyongbao_numbers


def get_huawei_download_number():
    url = "http://app.hicloud.com/app/C100011441"
    # 模拟浏览器请求网页，否则反爬虫会出现403错误
    headers = {
        'Cache-Control': "no-cache",
        'Postman-Token': "2a22cfc8-b89c-5847-36b9-2e62a9cfbbf3",
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
    }

    html_content = requests.request("GET", url, headers=headers)
    # print(html_content.content)
    # 解析网页标签
    encoding = "utf-8"
    soup = BeautifulSoup(html_content.content, "html.parser", from_encoding=encoding)
    # 通过类名查找
    # for itemText in soup.find_all('span', attrs={'class': 'grey sub'}):
    result = soup.find_all('span', attrs={'class': 'grey sub'})

    # 获取下载数量信息 eg：119次
    contents = result[0].contents.pop()
    # 分割字符串得到下载数量
    yingyongbao_numbers = contents[:len(contents) - 1][3:]
    print "华为商店下载：\t", yingyongbao_numbers
    # 返回下载数量信息
    return yingyongbao_numbers


if __name__ == '__main__':
    get_yingyongbao_download_number()
    get_huawei_download_number()
