# 如何使用glog

```cpp
   #include <glog/logging.h>

   int main(int argc, char* argv[]) {
     // Initialize Google's logging library.
     google::InitGoogleLogging(argv[0]);

     // ...
     LOG(INFO) << "Found " << num_cookies << " cookies";
   }
```

最简单

## 严重程度

`INFO`,`WARNING`,`ERROR`,`FATAL`.

FATAL会终止程序。

默认在`/tmp/<program name>.<hostname>.<user name>.log.<severity level>.<date>.<time>.<pid>`。只记FATAL和ERROR。

## 其他参数

按照`./your_application --logtostderr=1`。

有几个参数：

* logtostderr(bool, default=false) 把消息记到stderr里。
* stderrthreshold(int, default=2, which is ERROR)，把大于这个都copy到stderr里。
* `minloglevel` (`int`, default=0, which is `INFO`)记录这个以上的消息。
* `log_dir` (`string`, default="")路径
* `v` (`int`, default=0) 显示所有的 `VLOG(m)`
* `vmodule` (`string`, default="")。Per-module verbose level. The argument has to contain a comma-separated list of <module name>=<log level>. <module name> is a glob pattern (e.g., gfs* for all modules whose name starts with "gfs"), matched against the filename base (that is, name ignoring .cc/.h./-inl.h). <log level> overrides any value given by --v. See also the section about verbose logging.

可以在程序里改，`FLAGS_*`

```cpp
   LOG(INFO) << "file";
   // Most flags work immediately after updating values.
   FLAGS_logtostderr = 1;
   LOG(INFO) << "stderr";
   FLAGS_logtostderr = 0;
   // This won't change the log destination. If you want to set this
   // value, you should do this before google::InitGoogleLogging .
   FLAGS_log_dir = "/some/log/directory";
   LOG(INFO) << "the same file";

```

## 条件记录

满足条件

```cpp
   LOG_IF(INFO, num_cookies > 10) << "Got lots of cookies";
```

每十次

```cpp
   LOG_EVERY_N(INFO, 10) << "Got the " << google::COUNTER << "th cookie";
```

结合

```cpp
   LOG_IF_EVERY_N(INFO, (size > 1024), 10) << "Got the " << google::COUNTER
                                           << "th big cookie";
```

前多少次

```cpp
   LOG_FIRST_N(INFO, 20) << "Got the " << google::COUNTER << "th cookie";
```

## 调试模式

只在debug模式有效，非debug模式啥都没有。

```cpp
   DLOG(INFO) << "Found cookies";

   DLOG_IF(INFO, num_cookies > 10) << "Got lots of cookies";

   DLOG_EVERY_N(INFO, 10) << "Got the " << google::COUNTER << "th cookie";
```

## `CHECK` 宏

类似`ASSERT`但是非DEBUG也行。

`CHECK_EQ`, `CHECK_NE`, `CHECK_LE`, `CHECK_LT`, `CHECK_GE`, and `CHECK_GT`. 比较两个值。会记录FATAL，还有两个值。还有`CHECK_NOTNULL`。

比较`char*`时候会有`CHECK_STREQ`, `CHECK_STRNE`,`CHECK_STRCASEEQ`, and `CHECK_STRCASENE`.case的大小写敏感的。

还有`CHECK_DOUBLE_EQ`可以容忍误差。 `CHECK_NEAR` 后接三个数，第三个是margin。

## 自定义优先级 v相关

## segmentation fault处理

加google::InstallFailureSignalHandler()

