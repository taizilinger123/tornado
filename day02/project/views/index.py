#!/usr/bin/env python
# -*- coding:utf-8 -*-
import tornado.web
from tornado.web import RequestHandler

class IndexHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.write("sunck is a good man")

class SunckHandler(RequestHandler):
    #该方法会在HTTP方法之前调用
    def initialize(self, word1, word2):
        self.word1 = word1
        self.word2 = word2

    def get(self, *args, **kwargs):
        print(self.word1, self.word2)
        self.write("sunck is a nice man")

