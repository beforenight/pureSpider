#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Administrator'
__date__ = '2018/1/15'

import socket


# host_name = socket.gethostbyname("127.0.0.1")
# print host_name
# host_name = socket.gethostname()
# print host_name


def print_machine_info():
    '''
    获取本机设备Ip地址
    :return:
    '''
    host_name = socket.gethostname()
    ip_address = socket.gethostbyname(host_name)
    print "Host name: %s" % host_name
    print "Ip Address: %s" % ip_address


def get_remote_machine_info(remote_host):
    '''
    获取远程设备的IP地址
    :return:
    '''
    try:
        print "Remote Host: %s" % remote_host
        print "Ip address: %s" % socket.gethostbyname(remote_host)
    except socket.error, err_msg:
        print "%s : %s" % (remote_host, err_msg)


if __name__ == '__main__':
    print_machine_info()
    remote_host = 'www.python.org'
    get_remote_machine_info(remote_host)
    # Error Host Name
    remote_host = 'www.python.or'
    get_remote_machine_info(remote_host)
