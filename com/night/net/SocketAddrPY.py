#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import sys


def resue_socket_addr():
    '''
    重用套接字地址
    :return:
    '''
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    old_state = s.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)
    print "Old socket state: %s" % old_state

    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    new_state = s.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)
    print "New socket state: %s" % new_state

    local_port = 8282
    srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind(('', local_port))
    srv.listen(1)
    print ("Listening on port: %s " % local_port)

    while True:
        try:
            connection, addr = srv.accept()
            print 'Connected by %s : %s' % (addr[0], addr[1])
        except KeyboardInterrupt:
            break
        except socket.error, msg:
            print "%s" % msg

    pass


if __name__ == '__main__':
    resue_socket_addr()
