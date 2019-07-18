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
            tornado.web.url(r'/kaige',index.KaigeHandler,{"word3":"handsome", "word4":"cool"},name="kaigegood"),

            #uri
            # (r'/liuyifei/(\w+)/(\w+)/(\w+)', index.LiuyifeiHandler),
            (r'/liuyifei/(?P<p1>\w+)/(?P<p3>\w+)/(?P<p2>\w+)', index.LiuyifeiHandler),

            #get
            (r'/zhangmanyu', index.ZhangmanyuHandler),

            #post
            (r'/postfile',index.PostFileHandler),

            #request对象
            (r'/zhuyin', index.ZhuyinHandler),

            #上传文件
            (r'/upfile', index.UpFileHandler),

        ]
        super(Application,self).__init__(handlers,**config.settings)