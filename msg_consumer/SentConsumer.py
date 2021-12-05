# -*- coding: utf-8 -*-
# @Time    : 2021/12/5 12:51
# @Author  : youyim
# @File    : SentConsumer.py
# @Software: PyCharm

from queue import Queue
import time

# 发送消息队列
sent_queue = Queue()


def build_queue_msg(msg):
    return msg


def sent_queue_msg(msg):
    sent_queue.put(msg)


# 发送消息消费者
def sent_msg_consumer(wechat_manager):
    while True:
        try:
            msg = sent_queue.get()
            if msg is not None:
                if msg["send_type"] == "text":
                    wechat_manager.SendText(msg["pid"], msg["wx_id"], msg["msg"])
                elif msg["send_type"] == "chatroomat":
                    wechat_manager.SendText(msg["pid"], msg["wx_id"], msg["msg"], msg.get("atlist",""))
                # 可以根据 wechat.py 里的接口，写其他发送类型的方法
        except Exception as e:
            pass
            # 发送失败的处理
        time.sleep(0.1)