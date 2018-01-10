#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup


# 获取coolapk.com应用分类统计
def get_coolapk_app_category_list():
    baseUrl = "https://www.coolapk.com/apk/"
    # // 请求链接
    requests_get = requests.get(baseUrl)

    # // 解析链接
    soup = BeautifulSoup(requests_get.content, "lxml")
    title = soup.find_all("div", class_="right_title")
    print title[0].span.text
    # 解析分类大标题
    title_first = soup.find_all("div", class_="type_list")
    # print title_first.pop()
    for item in title_first:
        # 打印一级标题
        print item.p.a.text
        # print  item.find_all('p', class_="type_title")
        # 打印二级标题
        print  item.find_all('p', class_="type_tag")[0].text


if __name__ == '__main__':
    get_coolapk_app_category_list()

    # 应用分类
    # 系统工具
    #
    # 输入法
    # 文件管理
    # 清理优化
    # 安全防护
    # 备份还原
    # 辅助加强
    #
    # 桌面插件
    #
    # 桌面
    # 插件
    # 锁屏
    #
    # 主题美化
    #
    # 壁纸
    # 图标
    # 字体
    # cm主题
    # layers主题
    # Substratum主题
    # xperia主题
    # emui主题
    # 开机动画
    #
    # 社交聊天
    #
    # 聊天
    # 微博
    # 交友
    # 论坛
    # 表情
    #
    # 资讯阅读
    #
    # 阅读器
    # 新闻
    # 漫画
    # 小说
    # 科普
    #
    # 通讯网络
    #
    # 拨号
    # 短信
    # 浏览器
    # 下载
    # 流量
    # 通讯录
    # 邮箱
    # 运营商
    # 通知
    # 路由
    # 录音
    # WIFI
    #
    # 影音娱乐
    #
    # 视频
    # 音乐
    # 电台
    # 铃音
    # 播放器
    # 直播
    #
    # 摄影图片
    #
    # 拍照
    # 美图
    # 图库
    #
    # 生活服务
    #
    # 天气
    # 美食
    # 快递
    # 日历
    #
    # 实用工具
    #
    # 计算器
    # 测量
    # 酷友作品
    # 刷机
    #
    # 文档商务
    #
    # office
    # 笔记
    #
    # 金融财经
    #
    # 理财
    # 银行
    # 股票
    # 记账
    #
    # 运动健康
    #
    # 运动
    # 医疗
    # 健身
    #
    # 学习教育
    #
    # 词典
    # 课程表
    # 考试
    # 外语
    # 儿童
    # 题库
    # 大学
    #
    # 旅行交通
    #
    # 导航
    # 地图
    # 交通
    # 旅游
    # 酒店
    # 打车
    # 公交
    # 火车
    # 飞机
    #
    # 购物
    #
    # 电商
    # 团购
    # 导购
    # 海淘
    # 购物
    #
    # Xposed模块
    #
    # xposed
    #
    # VR
    #
    # VR视频
    # VR游戏
    #
    # 其他
    #
    # 其他
