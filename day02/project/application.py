#!/usr/bin/env python
# -*- coding:utf-8 -*-
import tornado.web
import config
from views import index

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/',index.IndexHandler),
            (r'/sunck', index.SunckHandler, {"word1":"good", "word2":"nice"}),
            ()

        ]
        super(Application,self).__init__(handlers,**config.settings)