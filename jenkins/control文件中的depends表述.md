# control文件中的depends表述

有替换包的话就加一个竖线`|`。

其他几个字符`<<,<=,=,>=,>>`分别代表严格小于，小于等于，严格等于。。。。

```
Package: mutt
Version: 1.3.17-1
Depends: libc6 (>= 2.2.1), default-mta | mail-transport-agent
```

