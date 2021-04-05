# -*- coding: utf-8 -*-
# @Time    : 2021/4/5 18:26
# @Author  : youyim
# @File    : server.py
# @Software: PyCharm

from flask import Flask, request
from gevent import pywsgi


app = Flask(__name__)


'''
回调接口,处理基本的业务逻辑
request的相关属性见 https://blog.csdn.net/claroja/article/details/80691766
'''


@app.route('/', methods=['POST', "Get"])
def Wechat_API():
    if request.method == 'POST':
        request_object = request.json  # demjson.decode(request.data)
        message(request_object)
        return request_object

    else:
        return "<html><body>如果能看到这些内容,说明可以连接到回调接口了</body>"


def server(host='127.0.0.1', post='8888', on_message = None):
    global message
    message = on_message
    print("server begin")
    server = pywsgi.WSGIServer((host, post), app, log=None)
    server.serve_forever()
