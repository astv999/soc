import pytest
from common import readYaml
import os

from common import constants

if __name__ == '__main__':

    '''读取重跑次数,项目路径'''
    dit = readYaml.read(constants.TEST_CASE_YAML)
    dit2 = readYaml.read(constants.PROJECT_YAML)
    retrys = dit['retrys']
    modules = dit['testSuite']['module'].split(" ")
    command = ["-s", "-q", "--reruns", str(retrys), "--alluredir", "./reports/xml"]
    dirname = dit2['project']['path']


    print(dit)
    '''拼接路径'''
    for i in modules:
        i = dirname + '/testcase/' + i
        command.insert(4, i)
    print(command)

    '''执行pytest和allure命令'''
    pytest.main(command)
    os.system("allure generate --clean reports/xml -o  reports/html")

