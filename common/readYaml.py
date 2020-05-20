import yaml
import os


def read(yaml_name=None):
    # 获取当前脚本所在文件夹路径
    cur_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
    # 获取yaml文件路径
    yaml_path = os.path.join(cur_path, "config/" + yaml_name)
    # open方法打开直接读出来
    f = open(yaml_path, 'r', encoding='utf-8')
    cfg = f.read()
    # d = yaml.load(cfg, Loader=yaml.FullLoader)  # 用load方法转字典
    d = yaml.safe_load(cfg)
    return d
