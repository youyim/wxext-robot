# -*- coding: utf-8 -*-
# @Time    : 2021/12/5 12:51
# @Author  : youyim
# @File    : ReceiveConsumer.py
# @Software: PyCharm

from queue import Queue
from message.MessageProcessing import MessageProcessing
import threading
import time


# 接受消息队列
receive_message_queue = Queue()

# 限制重复 1s
message_exclude_repeat = ''

# 接受消息（生产者）
def on_message(message):  # 回调接口，e小天推过来的消息都可以在这里拿到
    print(message)
    global message_exclude_repeat
    message_str = str(message)
    if message_exclude_repeat:
        if message_str == message_exclude_repeat:
            return
    message_exclude_repeat = message_str
    receive_message_queue.put(message)

#处理任务
def task(): # 会阻塞后续任务的获取，改成多线程
    try:
        msg = receive_message_queue.get()
        return MessageProcessing(msg).message_process()
    except Exception as e:
        receive_message_queue.task_done()

# 接收消息消费者
def message_queue_consumer():
    while True:
        if receive_message_queue.qsize() > 0:
            threading.Thread(target=task).start()
        time.sleep(0.1)