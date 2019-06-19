# 查看及更改soname

```
查看soname：
objdump -p libcurl.so.3.0.0 | grep SONAME
更改soname：
patchelf --set-soname libnewname.so liboldname.so
更改依赖项：
patchelf --replace-needed liboriginal.so libreplacement.so my-program
```

