#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import ntplib
from time import ctime


def print_time():
    '''
    从网络获取服务器时间，并打印当前时间
    :return:
    '''
    ntp_client = ntplib.NTPClient()
    response = ntp_client.request('pool.ntp.org')
    print ctime(response.tx_time)
    pass


if __name__ == '__main__':
    print_time()
