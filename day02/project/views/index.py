#!/usr/bin/env python
# -*- coding:utf-8 -*-
import tornado.web
from tornado.web import RequestHandler

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

