# socat用法

ubuntu下安装：`sudo apt-get install socat`

\#socat udp4-listen:11161,reuseaddr,fork UDP:[监控服务器IP]:161

udp4-listen：在本地建立的是一个udp ipv4协议的监听端口；
reuseaddr，绑定本地一个端口；
fork，设定多链接模式，即当一个链接被建立后，自动复制一个同样的端口再进行监听

AT串口`/dev/ttyUSB1`映射到5555端口：

`socat -d -d /dev/ttyUSB1,raw,nonblock,ignoreeof,cr,echo=0 TCP4-LISTEN:5555,reuseaddr`

转发到minicom终端： `socat /dev/ttyUSB1,raw,nonblock,ignoreeof,cr,echo=0 /dev/ttyS1,raw`

转发到终端(电脑端)： `socat /dev/ttyUSB1,raw,nonblock,ignoreeof,cr,echo=0 /dev/tty,raw`

参考文档：http://www.dest-unreach.org/socat/doc/socat.html

http://salomi.blog.51cto.com/389282/272809

http://wenku.baidu.com/view/13080211ff00bed5b9f31ddb.html