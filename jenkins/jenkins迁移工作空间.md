# jenkins迁移工作空间

如果有jenkins服务在运行中，建议先停止jenkins服务。

然后拷贝数据到新路径，我迁移的路径为 /opt/ldkjdata/.jenkins，
cp /root/.jenkins /opt/ldkjdata/.jenkins

设置JENKINS_HOME环境变量参数
打开tomcat的bin目录，编辑catalina.sh文件，在第一行下面添加
export JENKINS_HOME=/opt/ldkjdata/.jenkins

并且在profile文件最后加入：
vi /etc/profile
在最后加入：
export JENKINS_HOME=/opt/ldkjdata/.jenkins
保存，退出后执行
source /etc/profile
让配置生效

然后启动jenkins，所有的插件，配置，job及备份全部已迁移。