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
            tornado.web.url(r'/kaige',index.KaigeHandler,{"word3":"handsome", "word4":"cool"},name="kaigegood")

        ]
        super(Application,self).__init__(handlers,**config.settings)