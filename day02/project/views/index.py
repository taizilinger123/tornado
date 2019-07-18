#!/usr/bin/env python
# -*- coding:utf-8 -*-
import tornado.web
from tornado.web import RequestHandler
import os
import config

class IndexHandler(RequestHandler):
    def get(self, *args, **kwargs):
        url = self.reverse_url("kaigegood")
        self.write("<a href='%s'>去另一个界面</a>"%(url))

class SunckHandler(RequestHandler):
    #该方法会在HTTP方法之前调用
    def initialize(self, word1, word2):
        self.word1 = word1
        self.word2 = word2

    def get(self, *args, **kwargs):
        self.write("sunck is a nice man")

class KaigeHandler(RequestHandler):
    def initialize(self, word3, word4):
        self.word3 = word3
        self.word4 = word4
    def get(self, *args, **kwargs):
        self.write("kaige is a nice man")

class LiuyifeiHandler(RequestHandler):
    def get(self, p1, p2, p3, *args, **kwargs):
        print(p1 + "-" + p2 + "-" + p3)
        self.write("liuyifei is a nice women")

class ZhangmanyuHandler(RequestHandler):
    def get(self, *args, **kwargs):
        alist = self.get_arguments("a")
        print(alist[0],alist[1])
        self.write("zhangmanyu is a good women")

#post
class PostFileHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render('postfile.html')
    def post(self, *args, **kwargs):
        name = self.get_argument("username")
        passwd = self.get_body_argument("passwd")
        hobbyList = self.get_body_arguments("hobby")
        print(name, passwd, hobbyList)
        self.write("sunck is a handsome man")

class  ZhuyinHandler(RequestHandler):
    def get(self, *args, **kwargs):
        print(self.request.method)
        print(self.request.host)
        print(self.request.uri)
        print(self.request.path)
        print(self.request.query)
        print(self.request.version)
        print(self.request.headers)
        print(self.request.body)
        print(self.request.remote_ip)
        print(self.request.files)
        self.write("zhuyin is a good women")

class  UpFileHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render('upfile.html')
    def post(self, *args, **kwargs):
        filesDict = self.request.files
        for inputname in filesDict:
            fileArr = filesDict[inputname]
            for fileObj in fileArr:
                #存储路径
                filePath = os.path.join(config.BASE_DIRS,'upfile/'+fileObj.filename)
                with open(filePath, "wb") as f:
                    f.write(fileObj.body)
        self.write("ok")

#http://localhost:8000/zhangmanyu?a=1&b=2&c=%20%20%20%20%203
#%20表示空格
#http://localhost:8000/zhangmanyu?a=1&a=2
#http://localhost:8000/postfile
#http://localhost:8001/zhuyin?a=1&b=2

