#!/usr/bin/env python
# -*- coding: utf-8 -*-

'a socket example which send echo message to server.'

import socket

ip_address = '192.168.1.161'

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
for data in ['Michael', 'Tracy', 'Sarah']:
    # 发送数据:
    s.sendto(data, (ip_address, 9999))
    # 接收数据:
    print s.recv(1024)
s.close()