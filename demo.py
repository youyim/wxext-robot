# -*- coding: utf-8 -*-
# @Time    : 2021/4/5 18:26
# @Author  : youyim
# @File    : demo.py
# @Software: PyCharm

from wechat import WechatAPI
import threading
from msg_consumer.SentConsumer import sent_msg_consumer
from msg_consumer.ReceiveConsumer import message_queue_consumer, on_message

wechat_manager = WechatAPI()  # 实例机器人
threading.Thread(target=wechat_manager.start, args=(on_message,)).start()  # 启动机器人服务
threading.Thread(target=message_queue_consumer).start()  # 消息处理服务
threading.Thread(target=sent_msg_consumer, args=(wechat_manager,)).start()  # 消息发送服务