# 如何进入容器

首先是用下面的命令，查看容器id

```
# docker ps
CONTAINER ID        IMAGE                             COMMAND                  CREATED             STATUS              PORTS                  NAMES
f0d0f3411804        moviemasher/moviemasher.rb        "config/docker/entry…"   4 days ago          Up 4 days                                  moviemasher_rb
f821f2b82725        moviemasher/angular-moviemasher   "docker-php-entrypoi…"   4 days ago          Up 4 days           0.0.0.0:8090->80/tcp   angular_moviemasher
```

然后用下面的命令进入容器，就可以使用bash命令浏览容器里的文件：

```
docker exec -it [CONTAINER ID] bash
```

