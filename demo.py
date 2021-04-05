# -*- coding: utf-8 -*-
# @Time    : 2021/4/5 18:26
# @Author  : youyim
# @File    : demo.py
# @Software: PyCharm

from server import server
from wechat import WechatAPI
import threading

def on_message(message):
    print(message)
    if message.get('type','') == 1:
        # 复读机
        wechat_manager.SendText(message['pid'], message['data']['fromid'], message['data']['msg'])
    if message.get('type','') == 37:
        # 自动通过好友
        wechat_manager.AgreeUser(message['pid'], message['data']['msg'])


wechat_manager = WechatAPI()  # 实例机器人
wechat_manager.start()  # 启动微信
Server=server(host='127.0.0.1', post=8889, on_message=on_message)  # 创建回调接口服务器
threading.Thread(target=Server).start()  # 启动回调接口服务器