# Slidev 工作目录

使用mySlidev脚本进行快速管理。

创建项目 `hello`：
```bash
python mySlidev.py --create -o hello
```

调试项目 `hello`：
```bash
python mySlidev.py --dev -i .\hello
```

构建项目 `hello`：
```bash
python mySlidev.py --build -i .\hello
```



构建+同步所有文件到服务器：
```bash
python mySlidev.py --build --update
```

构建+同步项目 `hello` 到服务器：
```bash
python mySlidev.py --build --update -i hello
```