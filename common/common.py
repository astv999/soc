'''一些公共函数'''
import os
import datetime

'''删除过期截图，expire设置过期天数'''
def delete_expire_screen(expire=3):
    screenlist = []
    for i in os.walk("../screen/"):
        screenlist = i[2]
    for i in screenlist:
        screentime = i.split("_")[0]
        now = datetime.datetime.now().strftime('%Y-%m-%d')
        now = datetime.datetime.strptime(now, '%Y-%m-%d')
        screentime = datetime.datetime.strptime(screentime, '%Y-%m-%d')
        path = "../screen/{}".format(i)
        if((now-screentime).days>expire):
            if os.path.exists(path):
                os.remove(path)
                print("该截图文件({})已被删除！".format(i))
            else:
                print("该截图文件({})不存在！".format(i))

