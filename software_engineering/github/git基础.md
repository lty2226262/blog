[TOC]

# 基础

## 初始化 git init

```
git init
```

初始化，通过`git add`命令跟踪文件。

```
git add *.c
git add LICENSE
git commit -m 'initial project version'
```

## 克隆现有的仓库 git clone

利用`git clone [url]`

## 检查当前文件状态 git status 

```
git status
```
主要能看到untracked files

## 状态简览 git status -s

`git status`输出的命令十分详细，如果需要缩写则使用`git status -s`或者`git status --short`，可以得到输出如下：

```shell
git status -s
 M	README
MM	Rakefile
A	lib/git.rb
M	lib/simplegit.rb
??	LICENSE.txt
```

新添加的未跟踪的文件前面有`??`标记，新添加到暂存区的前面有`A`标记,修改过的有`M`，可以有两个可以出现的位置，出现在右边的`M`表示该文件被修改了没放到暂存区，靠左的表示修改了且放到了暂存区。

## 忽略文件 gitignore

添加一些gitignore

```shell
$ cat .gitignore
*.[oa]
*~
```

第一行告诉Git忽略所有以`.o`或者`.a`结尾的文件。一般这类对象文件和存档文件都是编译过程中出现的。第二行告诉Git忽略所有以波浪符(~)结尾的文件。

看一个`.gitignore`文件的例子

```typescript
# no .a files
*.a
# but do track lib.a, even though you're ignoring .a files above
!lib.a
# only ignore the TODO file in the current directory, not subdir/TODO
/TODO
# ignore all files in the build/ directory
build/
# ignore doc/notes.txt, but not doc/server/arch.txt
doc/*.txt
# ignore all .pdf files in the doc/ directory
doc/**/*.pdf
 
```

gitignore的规范如下：

* 使用空行或者以`#`开头的行都会被Git忽略
* 可以使用标准的glob模式匹配
* 匹配模式可以以（/）开头防止递归
* 匹配模式可以以（/）结尾指定目录
* 要忽略制定模式以外的文件或者目录，可以在模式前加上叹号（！）取反

## glob模式（简化正则表达式）

简化了的正则表达式。星号`*`匹配零个或者多个任意字符；`[abc]`匹配任何一个在方框中的字符（这个例子中要么匹配一个a，要么匹配一个b，要么匹配一个c）；问号`?`表示只匹配一个任意字符；如果方括号中使用短划线分割两个字符，表示在这两个字符之间都可以匹配。（比如`[0-9]`表示匹配所有0到9的数字）。使用两个星号`**`表示其中的任意目录，比如`a/**/z`可以表示`a/z`,`a/b/z`或者`a/b/c/z`等。

## 查看已暂存和未暂存的修改 git diff

如果`git status`不能满足要求，想知道具体修改了什么地方，可以用`git diff`命令。

想要查看尚未暂存的文件更新了哪些部分，不加参数直接输入`git diff`。

该命令比较的是工作目录中当前文件和暂存区域快照之间的差异，

## 提交更新

`git commit -a`可以自动吧所有跟踪过的暂存起来一并提交，从而跳过`git add`步骤。

## 移除文件

要从git中移除某个文件,必须要从跟踪文件清单中移除。可以用`git rm`命令完成此项工作，连带从工作目录删除指定的文件，这样以后就不会出现在跟踪清单了。

仅仅删除文件的话，会发现“changes not staged for commit”。

如果删除之前修改过并且已经放到暂存区的文件则需要加`-f`。

另外一种情况是，我们想把文件从git仓库中删除（从暂存区删除），但仍希望保存在当前工作目录中，比如忘记添加`.gitignore`文件，不小心加了一大堆日志文件，使用这一方法非常有用。

```cpp
git rm --cached README
```

后面可以列出文件或者目录的名字，可以使用glob模式。比如：

```shell
git rm log/\*.log
```

注意到星号前面的反斜杠，因为git有自己的文件模式扩展匹配方式，所以我们不用shell来展开帮忙。此命令删除log/目录下扩展名为.log的所有文件。类似的比如：

```shell
git rm \*~
```

## 移动文件

`git mv`没什么用，因为git会自动跟踪文件变化。

## 查看提交历史

`git log`

如果不用任何参数的话，`git log`会按提交时间列出所有的更新，最近的更新排在最上面。

`git log`有许多选项。

一个常用的选项是`-p`，用来显示每次提交的内容差异。也可以加上-2来显示最近两次提交： 该选项除了显示基本信息之外，还附带了每次commit的变化。当进行代码审查时，就非常有用了。当想看到每次提交的简略的统计信息，可以使用`--stat`选项。

另外一个常用的选项是`--pretty`，这个选项可以指定使用不同于默认格式的方式展示提交历史。这个选项有一些内建的子选项供使用。例如用`oneline`将每个提交放在一行显示，查看的提交数很大时有用。另外还有`full`, `short`,`fuller`可以用。最有意思的是format，可以定制现实的消息记录格式。

```shell
 $ git log --pretty=format:"%h - %an, %ar : %s"
  ca82a6d - Scott Chacon, 6 years ago : changed the version number
  085bb3b - Scott Chacon, 6 years ago : removed unnecessary test
  a11bef0 - Scott Chacon, 6 years ago : first commit
```

`git log --pretty=format`常用的选项列出了常用占位符写法及其代表的意义。

| 选项 | 说明                                   |
| ---- | -------------------------------------- |
| %H   | 提交对象(commit)的完整哈希字串         |
| %h   | 提交对象的简短哈希字串                 |
| %T   | 树对象(tree)的完整哈希字串             |
| %t   | 树对象的简短哈希字串                   |
| %P   | 父对象(parent)的完整哈希字串           |
| %p   | 父对象的简短哈希字串                   |
| %an  | 作者名字                               |
| %ae  | 作者邮箱地址                           |
| %ad  | 作者修订日期(可以用—date=选项定制格式) |
| %ar  | 作者修订日期，按多久以前的方式显示     |
| %cn  | 提交者的名字                           |
| %ce  | 提交者的email                          |
| %cd  | 提交日期                               |
| %cr  | 提交日期，按多久以前的方式显示         |
| %s   | 提交说明                               |

可以配合`--graph`结合一起使用/这个选项添加了一些ASCII字符串来形象地展示分支、合并历史。

```shell
   $ git log --pretty=format:"%h %s" --graph
  * 2d3acf9 ignore errors from SIGCHLD on trap
  *  5e3ee11 Merge branch 'master' of git://github.com/dustin/grit
  |\
  | * 420eac9 Added a method for getting the current branch.
  * | 30e367c timeout code and tests
  * | 5a09431 add timeout protection to grit
  * | e1193f8 support for heads with slashes in them
  |/
  * d6016bc require time for xmlschema
  *  11d191e Merge branch 'defunkt' into local
```

git log 的常用选项

| 选项           | 说明                                          |
| -------------- | --------------------------------------------- |
| -p             | 按补丁格式显示每个更新之间的差异              |
| —stat          | 显示每次更新的文件修改统计信息                |
| —shortstat     | 只显示—stat中最后的行数修改添加移除统计       |
| —name-only     | 仅在提交信息后显示已修改的文件清单。          |
| —name-status   | 显示新增、修改、删除的文件清单。              |
| —abbrev-commit | 仅显示sha-1的前几个字符，而非所有的40个字符。 |
| —relative-date | 使用较短的相对时间显示                        |
| —graph         | 显示ascii图形表示的分支合并历史               |
| —pretty        | 使用其他格式显示                              |

## 限制输出长度

可以显示部分提交信息。

`git log -2`最近两条

还有按照时间,有—since和--until

```shell
git log —since=2.weeks
```

`—author`显示指定作者提交，`--grep`搜索提示说明中的关键字。如果同时满足两个选项则需要用`--all-match`。

另一个非常有用的筛选选项是`-S`，可以列出那些添加或移除某些字符串的提交。比如说，想找出添加或者删除某一个特定函数的引用的提交，可以这样使用：

```shell
$ git log -Sfunction_name
```

最后一个很实用的`git log`选项是路径(path), 如果只关心某些文件或者目录的历史提交，可以在git log选项的最后指定它们的路径。因为是放在最后位置上的选项，所以两个短划线（--）隔开之前的选项和后面限定的路径名。

限制git log输出的选项

| 选项           | 说明                                 |
| -------------- | ------------------------------------ |
| -(n)           | 仅显示最近的n条提交                  |
| —since,—after  | 仅显示指定时间之后的提交。           |
| —until,—before | 仅显示指定时间之前的提交。           |
| —author        | 仅显示指定作者相关的提交。           |
| —committer     | 仅显示指定提交者相关的提交。         |
| —grep          | 仅显示含指定关键字的提交。           |
| -S             | 仅显示添加或移除了某个关键字的提交。 |

举例子，2008年10月期间，Junio Hamano提交但未合并的测试文件。

```shell
$ git log --pretty="%h - %s" --author=gitster --since="2008-10-01" \
     --before="2008-11-01" --no-merges -- t/
  5610e3b - Fix testcase failure when extended attributes are in use
  acd3b9e - Enhance hold_lock_file_for_{update,append}() API
  f563754 - demonstrate breakage of detached checkout with symbolic link
  HEAD
  d1a43f2 - reset --hard/read-tree --reset -u: remove unmerged new paths
  51a94af - Fix "checkout --track -b newbranch" on detached HEAD
  b0ad11e - pull: allow "git pull origin $something:$current_branch" into an
  unborn branch
 
```

## 撤销操作

