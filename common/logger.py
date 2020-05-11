# coding=utf-8
import logging.config
import os
from common import readYaml
from common import path
from common import constants

os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))


class Logger:

    def __init__(self, logger=None):
        self.logger = logging.getLogger(logger)
        default_level = logging.INFO
        path_dir = path.getcwd() + '/config/' + constants.LOGGING_YAML
        if os.path.exists(path_dir):
            with open(path_dir, 'rt', encoding="utf-8") as f:
                config = readYaml.read(constants.LOGGING_YAML)
            config['handlers']['info_file_handler']['filename'] = path.getcwd() + '/' \
                                                                  + config['handlers']['info_file_handler']['filename']
            config['handlers']['error_file_handler']['filename'] = path.getcwd() + '/' \
                                                                  + config['handlers']['error_file_handler']['filename']
            logging.config.dictConfig(config)
        else:
            logging.basicConfig(level=default_level)
            print("该yaml日志配置文件不存在,请检查路径")

    def getLogger(self):
        return self.logger
