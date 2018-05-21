# 起步

## 初次运行git的配置

有三层，

* `/etc/gitconfig`文件，包含系统上每一个用户及他们仓库的通用配置。带有`--system`选项在这里读写。
* `~/.gitconfig`或者`~/.config/git/config`只针对当前用户。可以传递`--global`选项让git读写此文件。
* 当前使用仓库的git目录中的config文件：(`.git/config`):针对该仓库。

每一个级别覆盖上一级别的配置，所以`.git/config`会覆盖`/etc/gitconfig`中的配置。

## 用户信息

```
git config --global user.name "Joey Liu"
git config --global user.emali lty2226262@gmail.com
```
如果用了`--global`只需要配置一次，之后就会一直调用。

## 文本编辑器

```
git config --global core.editor emacs
git config --global core.editor vim
```

## 检查配置信息

```
git config --list
user.name=John Doe
user.email=johndoe@example.com
color.status=auto
color.branch=auto
color.interactive=auto
color.diff=auto
```

可能会看到重复的，因为从`/etc/gitconfig`和`~/.gitconfig`同时读。用最后一个。

## 帮助

```
git help <verb>
git <verb> --help
man git-<verb>
```

如果想要获得config命令的手册，执行
```
git help config
```
