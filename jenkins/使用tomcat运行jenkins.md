1. 在tomcat官网下载tomcat。
2. 解压到/opt/下面
3. 更改conf/server.xml配置文件可以改端口
4. 生成supervisor配置文件

```
[program:tomcat]
command=/root/tools/apache-tomcat-7.0.70/bin/catalina.sh run
stdout_logfile=/root/tools/apache-tomcat-7.0.70/logs/catalina.out
autostart=true
autorestart=true
startsecs=5
priority=1
stopasgroup=true
killasgroup=true
```

5.配置管理员的权限

```
sudo vim conf/tomcat-users.xml
<role rolename="manager-gui"/>
<role rolename="admin-gui"/>
<user username="root" password="123456" roles="manager-gui,admin-gui"/>
```
6. 下载jenkins
7. 解压到tomcat的webapp下。
8. 加一个ln -s jenkins/ ROOT/
9. 访问127.0.0.1:8089/
10. 

