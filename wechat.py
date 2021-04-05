# -*- coding: utf-8 -*-
# @Time    : 2021/4/5 18:26
# @Author  : youyim
# @File    : wechat.py
# @Software: PyCharm


import requests
import json
import xmltodict


class WechatAPI(object):
    def __init__(self):
        """
        类初始化函数
        :param on_message: 收到微信消息时的回调函数
        """
        self.url = "http://127.0.0.1:8203/api?json"
        self.params = {"key":self.get_key()}

    def start(self):
        """
        启动http服务
        """
        boot = self.bootwechat()  # 初始化微信连接
        print('boot:' + str(boot))
        self.ShowWX(boot['pid'])

    def postApi(self, data):
        """
        功能API接口
        :param data: 传递给接口的数据
        :return: 接口返回的数据
        """
        response = requests.post(url=self.url, data=data, params=self.params)
        if response:
            return response.json()
        return 0

    # 启用一个微信,已检测到微信直接启用,否则启动一个新的
    def bootwechat(self):
        """
        启用一个微信,已检测到微信直接启用,否则启动一个新的
        """
        data = {
            "method": "run",
            "pid": 0
        }
        return self.postApi(data)

    def AddWechat(self):
        """
        启用一个微信,已检测到微信直接启用,否则启动一个新的
        """
        data = {
            "method": "run",
            "pid": -1
        }
        return self.postApi(data)

    # 抖动微信窗口
    def ShowWX(self, pid):
        """
        抖动微信窗口
        """
        data = {
            "method": "show",
            "pid": pid
        }
        return self.postApi(data)

    # Kill掉当前进程，以备不时之需
    def KillWX(self, pid):
        """
        Kill掉当前进程
        """
        data = {
            "method": "kill",
            "pid": pid
        }
        return self.postApi(data)

    # 获取用户登录信息
    def GetUserInfo(self, pid):
        """
        获取用户登录信息
        """
        data = {
            "method": "getInfo",
            "pid": pid
        }
        return self.postApi(data)

    # 获取用户通讯录
    def GetAllList(self, pid):
        """
        获取用户通讯录
        """
        data = {
            "method": "getUser",
            "pid": pid
        }
        return self.postApi(data)

    # 发送文本消息
    def SendText(self, pid, wxid, msg, atid=""):
        """
        发送文本消息
        :param wxid: 发给谁（wx_id）
        :param msg: 发给什么（msg）
        :return: 接口返回的数据
        """
        data = {
            "method": "sendText",
            "wxid": wxid,
            "msg": msg,
            "atid": atid,
            "pid": pid
        }
        return self.postApi(data)

    # 获取群聊列表
    def GetGroup(self, pid):
        """
        获取群聊列表
        """
        data = {
            "method": "getGroup",
            "pid": pid
        }
        return self.postApi(data)

    # 获取群聊成员列表
    def GetGroupUser(self, pid, chatroom):
        """
        获取群聊成员列表
        :param chatroom: 群聊id（chatroom）
        :return: 返回群聊成员信息
        """
        data = {
            "method": "getGroupUser",
            "wxid": chatroom,
            "pid": pid
        }
        return self.postApi(data)

    # 设置群公告
    def SetRoomAnnouncement(self, pid, chatroom, msg):
        """
        设置群公告
        :param chatroom: 群聊id（chatroom）
        :param msg: 公告内容（msg）
        :return: 返回接口信息
        """
        data = {
            "method": "setRoomAnnouncement",
            "wxid": chatroom,
            "msg": msg,
            "pid": pid
        }
        return self.postApi(data)

    # 设置备注
    def SetRemark(self, pid, wxid, name):
        """
        设置备注
        :param wxid: 好友wxid（wxid）
        :param name: 好友新备注（name）
        :return: 返回接口信息
        """
        data = {
            "method": "setRemark",
            "wxid": wxid,
            "msg": name,
            "pid": pid
        }
        return self.postApi(data)

    # 群聊邀请
    def SendGroupInvite(self, pid, chatroom, wxid):
        """
        群聊邀请
        :param chatroom: 邀请群聊id（chatroom）
        :param wxid: 被邀请好友wxid（wxid）
        :return: 返回接口信息
        """
        data = {
            "method": "sendGroupInvite",
            "wxid": chatroom,
            "msg": wxid,
            "pid": pid
        }
        return self.postApi(data)

    # 修改群名称
    def setRoomName(self, pid, chatroom, name):
        """
        修改群名称
        :param chatroom: 群聊id（chatroom）
        :param name: 需要修改的名称（name）
        :return: 返回接口信息
        """
        data = {
            "method": "setRoomName",
            "wxid": chatroom,
            "msg": name,
            "pid": pid
        }
        return self.postApi(data)

    # 退出群聊
    def QuitChatRoom(self, pid, chatroom):
        """
        退出群聊
        :param chatroom: 需要推出的群聊id（chatroom）
        :return: 返回接口信息
        """
        data = {
            "method": "quitChatRoom",
            "wxid": chatroom,
            "pid": pid
        }
        return self.postApi(data)

    # 发送文件 支持file和url，file：路径记得将\转为\\，url则是链接
    def SendFile(self, pid, wxid, file, fileType="file"):
        """
        发送文件
        支持file和url，file：路径记得将\转为\\，url则是链接
        :param wxid: 需要发给谁（wxid）
        :param file: 需要发送的文件（file）
        :param fileType: 发送的文件类型（本地文件或者网络图片）（fileType）
                         默认发送本地文件
                         如需要设置发送网络图片需设置：fileType="url"
        :return: 返回接口信息
        """
        data = {
            "method": "sendFile",
            "wxid": wxid,
            "file": file,
            "fileType": fileType,
            "pid": pid
        }
        return self.postApi(data)

    # 发送图片 支持file和url，file：路径记得将\转为\\，url则是链接
    def SendImage(self, pid, wxid, file, fileType="file"):
        """
        发送图片
        支持file和url，file：路径记得将\转为\\，url则是链接
        :param wxid: 需要发给谁（wxid）
        :param file: 需要发送的图片（file）
        :param fileType: 发送的文件类型（本地文件或者网络图片）（fileType）
                         默认发送本地文件
                         如需要设置发送网络图片需设置：fileType="url"
        :return: 返回接口信息
        """
        data = {
            "method": "sendImage",
            "wxid": wxid,
            "img": file,
            "imgType": fileType,
            "pid": pid
        }
        return self.postApi(data)


    # 删除好友
    def DeleteUser(self, pid, wxid):
        """
        删除好友
        :param wxid: 删除好友的wxid（wxid）
        :return: 返回接口信息
        """
        data = {
            "method": "deleteUser",
            "wxid": wxid,
            "pid": pid
        }
        return self.postApi(data)

    # 移除群聊
    def DelRoomMember(self, pid, chatroom, wxid):
        data = {
            "method": "delRoomMember",
            "wxid": chatroom,
            "msg": wxid,
            "pid": pid
        }
        return self.postApi(data)


    # 同意添加好友
    def AgreeUser(self, pid, msg):
        """
        同意添加好友
        :param msg: 好友请求消息里的msg
        :return: 返回接口信息
        """
        msg_dict = json.loads(json.dumps(xmltodict.parse(msg)))
        encryptusername = msg_dict['msg']['@encryptusername']
        ticket =  msg_dict['msg']['@ticket']
        scene =  msg_dict['msg']['@scene']
        data = {
            "method": "agreeUser",
            "encryptusername": encryptusername,
            "ticket": ticket,
            "scene": scene,
            "pid": pid
        }
        return self.postApi(data)

    def SendArticle(self, pid, wxid, xml):
        """
        同意添加好友
        :wxid: 需要发给谁（wxid）
        :xml: 需要发送的xml，可以直接转发消息回调接口消息里的xml
        """
        data = {
            "method": "sendArticle",
            "wxid": wxid,
            "xml": xml,
            "pid": pid
        }

        return self.postApi(data)

    def environment_variable(self):
        with open(r'C:\Users\Public\Documents\wxext.cn\WxExt.ini', encoding='utf-8') as f:
            data = f.read()
        return json.loads(data)

    def get_key(self):
        data = self.environment_variable()
        return data["key"]

    def ListWechat(self):
        data = {
            "method": "list"
        }

        return self.postApi(data)

    def KillWechat(self, pid):
        data = {
            "method": "kill",
            "pid": pid
        }
        return self.postApi(data)

    def Get_HttpNotify(self):
        data = {
            "method": "notify"
        }
        return self.postApi(data)
