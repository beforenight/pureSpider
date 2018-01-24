#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Administrator'
__date__ = '2018/1/24'

import time


def show_time_list():
    times = []
    # 当前时间
    t0 = time.clock()
    for mtime in range(1, 20000):
        times.append(mtime)
    print time.clock() - t0, ' seconds progress'
    pass


def show_time_list2():
    times = []
    # 当前时间
    t0 = time.clock()
    b = [mtime for mtime in range(1, 20000)]
    print time.clock() - t0, ' seconds progress'
    pass


def show_list_range():
    '''
    列表推导式
    :return:
    '''
    a = [i ** 2 for i in range(1, 10)]
    print a
    c = [j + 1 for j in range(1, 10)]
    print c

    k = [n for n in range(1, 20) if n % 2 == 0]
    print k

    z = [letter.lower() for letter in 'ASDFGHJKWERTYUI']
    print z
    pass


def show_dirc_range():
    '''
    字典推导式
    :return:
    '''
    letters = {'A': 'a', 'B': 'b', 'C': 'c'}
    d = {i: i + 1 for i in range(4)}
    print d

    g = {i: j for i, j in zip(range(1, 6), 'abcdef')}
    print g

    g = {i: j.upper() for i, j in zip(range(1, 6), 'abcdef')}
    print g

    pass


if __name__ == '__main__':
    list = []
    for item in range(0, 20, 2):
        list.append(item)
    # print list
    show_time_list()
    show_time_list2()
    show_list_range()
    show_dirc_range()
