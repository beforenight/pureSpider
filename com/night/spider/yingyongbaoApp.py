#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Administrator'
__date__ = '2018/1/9'
import requests
from bs4 import BeautifulSoup


# 爬取应用宝市场App下载量
def get_app_download_num(apkId):
    # 应用宝app详情页面
    base_url = 'http://sj.qq.com/myapp/detail.htm?apkName=' + apkId
    # 请求页面
    requests_get = requests.get(base_url)
    # 解析网页源码
    soup = BeautifulSoup(requests_get.content, 'lxml')
    # 找到app名称标签
    all_names = soup.find_all("div", class_="det-name-int")
    print "App名称：\t", all_names[0].text
    # 找到下载量标签
    all_infos = soup.find_all("div", class_="det-ins-num")
    # print all_infos[0].text
    # print all_infos[0].text[-2:]
    # 切片
    print "下载量：\t", all_infos[0].text[:-2], "次"


if __name__ == '__main__':
    # app包名，唯一标示
    apkId = "com.tencent.mobileqq"
    get_app_download_num(apkId)
    apkId = "com.devilk.RunGirl"
    get_app_download_num(apkId)
