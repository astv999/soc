# coding=utf-8

import os


def getcwd():
    # 获取当前脚本所在文件夹路径
    cur_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
    return cur_path
