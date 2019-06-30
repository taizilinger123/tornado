#!/usr/bin/env python
# -*- coding:utf-8 -*-

import tornado.web
from tornado.web import RequestHandler

class IndexHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.write("sunck is a good man")