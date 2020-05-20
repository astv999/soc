import pytest
import os
import platform
from common import constants
from common import readYaml

if __name__ == '__main__':
    dirname = os.path.abspath(os.path.dirname(__file__))
    '''读取重跑次数,项目路径'''
    dit = readYaml.read(constants.TEST_CASE_YAML)
    retrys = dit['retrys']
    modules = dit['testSuite']['module'].split(" ")
    command = ["-s", "-q", "--reruns", str(retrys), "--alluredir", "./reports/xml"]

    '''拼接路径'''
    for i in modules:
        i = dirname + '/testcase/' + i
        command.insert(4, i)
    print(command)

    '''执行pytest和allure命令'''
    pytest.main(command)
    reportsXMLDir = dirname + "/reports/xml";
    reportsHTMLDir = dirname + "/reports/html";
    allureExecutable = "allure.bat"
    '''如果是mac操作系统，则更换allure可执行文件名称'''
    if platform.system() == 'Darwin':
        allureExecutable = "allure"
    os.system(dirname + "/tools/allure-2.7.0/bin/" + allureExecutable +
              " generate --clean " + reportsXMLDir + " -o  " + reportsHTMLDir)
    '''如果不需要每次都打开浏览器查看报告，把下面这行注释即可'''
    os.system(dirname + "/tools/allure-2.7.0/bin/" + allureExecutable + " open " + reportsHTMLDir)


