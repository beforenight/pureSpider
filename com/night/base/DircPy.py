#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Administrator'
__date__ = '2018/1/24'


def show_dirc():
    """
    字典相关操作
    :return:
    """
    dircs = {'A': 'a', 'B': 'b'}
    print dircs
    print dircs['A']
    dircs['C'] = 'C'
    print dircs
    # dirc不能进行切片
    # print dircs[0:2]
    pass


def show_set():
    '''
    集合相关集合
    :return:
    '''
    a_set = {1, 2, 3, 'a'}
    print a_set
    # 不能被索引或者切片
    # print a_set[0:2]
    # 添加
    a_set.add(5)
    # 删除
    a_set.discard(1)
    print a_set
    pass


def show_sort():
    '''
    排序
    :return:
    '''
    num_list = [2, 3, 'a', 66, 33, 1, 2, 3, 5, 6, 6, ]
    print num_list
    # 顺序
    sorted_list = sorted(num_list)
    print sorted_list
    # 倒序
    reverseed_list = sorted(num_list, reverse=True)
    print reverseed_list
    # 如果同时需要两个列表 使用Zip高级函数
    for a, b in zip(sorted_list, reverseed_list):
        print (a, 'is', b)
    pass


if __name__ == '__main__':
    show_dirc()
    show_set()
    show_sort()
