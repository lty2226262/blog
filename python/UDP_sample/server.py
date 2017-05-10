#!/usr/bin/env python
# -*- coding: utf-8 -*-

'a udp server example which send time to client.'

import socket


ip_address = '192.168.192.167'

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 绑定端口:
s.bind((ip_address, 9999))
print 'Bind UDP on 9999...'
while True:
    # 接收数据:
    data, addr = s.recvfrom(1024)
    print 'Received from %s:%s.' % addr
    # s.sendto('Hello, %s!' % data, addr)
