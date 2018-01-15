#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Administrator'
__date__ = '2018/1/15'
import socket
from binascii import hexlify


# inet_aton()、inet_ntoa()
def convert_ip4_address():
    '''
    格式化IPv4地址
    hexlify() 以十六进制显示二进制数据
    :return:
    '''
    for ip_addr in ['127.0.0.1', '192.168.0.1']:
        packed_ip_addr = socket.inet_aton(ip_addr)
        unpacked_ip_addr = socket.inet_ntoa(packed_ip_addr)
        print "IP Address: %s => Packed: %s, Unpacked: %s" % (ip_addr, hexlify(packed_ip_addr), unpacked_ip_addr)


def find_service_name():
    '''
    调用函数getservbyport()解析端口
    :return:
    '''
    protocolname = 'tcp'
    for port in [80, 25]:
        print "Port: %s => service name:%s " % (port, socket.getservbyport(port, protocolname))
    print "Port: %s => service name:%s " % (53, socket.getservbyport(53, 'udp'))


if __name__ == '__main__':
    convert_ip4_address()
    find_service_name()
