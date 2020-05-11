# pytest+selenium+allure2框架
## 技术选型及版本
- pytest:3.6.0
- selenium:3.141.0
- pytest-allure-adaptor:1.7.10
- pytest-rerunfailures:5.0


## allure常用函数

- allure.severity("优先级")
- allure.feature("模块名")
- allure.story("功能名")
- allure.step("步骤")
- allure.attach("用例参数")

## yaml配置文件
- logging.yaml  配置日志输出格式
- project.yaml  配置项目绝对路径
- testcase.yaml 配置用例相关（需执行用例文件，重跑次数）

## 配置环境变量
- allure-2.7.0/bin
- chromedriver

## 待实现功能
- 告罄功能
- 邮件功能
- 数据库校验
- 数据驱动（参数化）

## 以下是优化参考配置项
--------------------------------
- venv 已经集成 mac 和 windows 下的环境，不需要额外安装其它环境

## 为提升访问速度，切换yum源
```shell script
cd ~
mkdir .pip
cd .pip
touch pip.conf
vim pip.conf 添加如下内容
-------------
[global]
index-url = https://mirrors.aliyun.com/pypi/simple/
[install]
trusted-host=mirrors.aliyun.com
```

## 安装venv虚拟环境
```shell script
# 安装virtualenv
pip3 install virtualenv
# 创建独立运行环境 
virtualenv venv 
# 此时进入虚拟环境
source venv/bin/activate
# 退出venv环境 
deactivate
```

## 安装依赖环境
```shell script
sudo pip3  --default-timeout=100 install pytest==3.6.0
sudo pip3  --default-timeout=100 install pyyaml
sudo pip3  --default-timeout=100 install selenium==3.141.0
sudo pip3  --default-timeout=100 install pytest-allure-adaptor==1.7.10
sudo pip3  --default-timeout=100 install pytest-rerunfailures==5.0
```

