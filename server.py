#!/usr/bin/env python
# -*- coding:utf-8 -*-
import tornado.web
import tornado.ioloop

#类比Django中的视图
class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write("sunck is a good man")


if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/",IndexHandler)
    ])
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()