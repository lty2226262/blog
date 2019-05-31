# jenkins构建

1. 安装git插件
2. 构建一个自由风格的软件项目
3. use custom workspace directory: 
4. 选git
5. 在build里执行shell

```
#! /bin/bash
bash -c "cd /home/joey/jenkins_ws && source /opt/ros/melodic/setup.bash && catkin_make install"
```

