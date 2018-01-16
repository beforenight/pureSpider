#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket

SEND_BUF_SIZE = 4096
RECV_BUF_SIZE = 4096


def modify_buff_size():
    '''
    修改套接字的发送和接收缓冲区大小
    :return:
    '''
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Get the sixe of the socket1s send buffer
    # 获取套接字对象的属性
    bufsize = sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
    print "Buffer zise [Before]: %s" % bufsize

    # 修改套接字对象的属性
    sock.setsockopt(socket.SOL_TCP, socket.TCP_NODELAY, 1)
    sock.setsockopt(
        socket.SOL_SOCKET,
        socket.SO_SNDBUF,
        SEND_BUF_SIZE)
    sock.setsockopt(
        socket.SOL_SOCKET,
        socket.SO_RCVBUF,
        RECV_BUF_SIZE)

    bufsize = sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
    print "Buffer zise [After]: %s" % bufsize
    pass


def test_socket_modes():
    '''
    修改套接字设置为阻塞模式或非阻塞模式
    :return:
    '''
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setblocking(1)
    s.settimeout(0.5)
    s.bind(("127.0.0.1", 0))

    socket_address = s.getsockname
    print "Trival Server launched on socket: %s" % str(socket_address)
    while (1):
        s.listen(1)
    pass


if __name__ == '__main__':
    modify_buff_size()
    test_socket_modes()
