#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import struct
import sys
import time

# 客户端要连接的服务器地址
NTP_SERVER = "o.uk.pool.ntp.org"
# 指1970年1月1日，也叫Epoch
TIME1970 = 2208988800L


def sntp_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    data = '\x1b' + 47 * '\0'

    client.sendto(data, (NTP_SERVER, 123))
    data, address = client.recvfrom(1024)

    if data:
        print 'Response receiverd from：', address
    t = struct.unpack('!12T', data)[10]
    t -= TIME1970
    print '\tTime = %s' % time.ctime(t)
    pass


if __name__ == '__main__':
    sntp_client()
