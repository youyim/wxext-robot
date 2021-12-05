# -*- coding: utf-8 -*-
# @Time    : 2021/12/5 12:50
# @Author  : youyim
# @File    : MessageProcessing.py
# @Software: PyCharm

from msg_consumer.SentConsumer import build_queue_msg, sent_queue_msg
import logging

logging.basicConfig(level=logging.INFO)


# 消息解析
class MessageProcessing:

    def __init__(self, message_data):
        self.message = message_data.get("data", {})
        self.pid = message_data.get("pid", 0)
        self.myid = message_data.get('myid', '')
        self.type = message_data.get('type', '')
        self.method = message_data.get('method', '')
        # single
        self.msgid = self.message.get('id', '')
        self.wx_id = self.message.get('fromid', '')
        self.to_wxid = self.message.get('toid', '')
        self.msgcontent = self.message.get('msg', '')
        # sendinfo
        self.wx_id_search = self.message.get('alias', '')
        self.wx_nickname = self.message.get('nickName', '')
        self.remark_name = self.message.get('reMark', '')
        self.chatroomid = ""
        self.is_recv = not (self.myid == self.wx_id)
        self.option = {"pid": self.pid}
        self.source = self.message.get('source', '')
        if '@chatroom' in self.wx_id:
            # msgfrominfo
            self.chatroomid = self.wx_id
            self.wx_id = self.message.get('memid', '')
            self.nickName2 = self.message.get('nickName2', '')

    def message_process(self):
        if self.chatroomid:
            self.chatroom_message()
        else:
            if 'gh_' in self.wx_id:
                return
            self.single_message()

    # 个人消息
    def single_message(self):
        if not self.is_receive():
            return
        response_msg = ''
        # 文字消息
        response_msg = self.deal_single()

        if response_msg:
            response_msg["pid"] = self.pid
            response_msg["wx_id"] = self.wx_id
            sent_queue_msg(build_queue_msg(response_msg))

    def deal_single(self):
        print("收到私聊消息：", self.message)
        # 开始处理
        # ...
        if self.type == 1:
            return {'send_type': 'chatroomat', 'msg': self.msgcontent}  # 这是一个文本消息复读机例子
        # send_type 用于发送消息时判断用什么接口发
        # return 把处理后需要发送的内容返回回去

    # 群消息
    def chatroom_message(self):
        if not self.is_receive():
            return
        response_msg = ''
        # 文字消息
        response_msg = self.deal_chatroom()

        if response_msg:
            response_msg["pid"] = self.pid
            response_msg["wx_id"] = self.chatroomid
            sent_queue_msg(build_queue_msg(response_msg))

    def deal_chatroom(self):
        print("收到群聊消息：", self.message)
        # 开始处理
        # ...
        if self.type == 1:
            return {'send_type': 'chatroomat', 'msg': self.msgcontent, 'atlist': self.wx_id}  # 这是一个文本消息复读机并@发送人 例子，
        # send_type 用于发送消息时判断用什么接口发
        # 把处理后需要发送的内容返回回去

    def is_receive(self):  # 判断是否是自己发送的消息
        if self.is_recv:
            return True
        return False
