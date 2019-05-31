# how to use
1、安装python环境，执行 python-3.6.3-amd64.exe，注意勾选add python 3.6 to PATH

> 参考链接：
> https://jingyan.baidu.com/article/aa6a2c148024200d4d19c410.html

若已经安装python， 可略过此步骤

2、使用windows键+R组合键，打开窗口，输入cmd，确定后进入dos环境

3、执行命令，安装环境依赖
```
pip install xlwt
```

4、dos环境下，切换当前路径到脚本存放路径
```
cd /d F:\test_demo\ApkPermissionCheck
```

4、执行检查脚本,比如要检查 \\192.168.2.123\休闲游戏\Kyuktu 目录下的游戏权限
```bash
python main.py "\\192.168.2.123\休闲游戏\Kyuktu"
```

5、执行结束后会在脚本目录下生成一个xlsx文件

6、结束