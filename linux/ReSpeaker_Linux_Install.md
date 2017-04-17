https://github.com/respeaker/get_started_with_respeaker/blob/master/Introduction.md#hardware

sudo apt-get update

sudo apt-get install git-core curl build-essential openssl libssl-dev

下载并解压 node-v4.4.4-Linux-x64.tar.xz

输入命令：vim /etc/profile（如果没有安装vim，可根据提示安装，vim比vi好用多了），在末尾添加以下三行：

export NODE_HOME=/opt/node

export PATH=$PATH:$NODE_HOME/bin 

export NODE_PATH=$NODE_HOME/lib/node_modules

在命令行输入：vim /root/.bashrc,并在文件末尾加入一行source etc/profile命令，保存。这样就大功告成了。

npm config set registry http://registry.npm.taobao.org

git clone https://github.com/Fuhua-Chen/ReSpeaker-Microphone-Array-HID-tool.git
sudo chmod 777 ./install_linux.sh
./install_linux.sh
