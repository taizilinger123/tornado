#!/usr/bin/env python
# -*- coding:utf-8 -*-
import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options


tornado.options.define("port",default=8000,type=int)
tornado.options.define("list",default=[],type=str,multiple=True)

class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write("sunck is a good man")

if __name__ == "__main__":
    tornado.options.parse_config_file("config")
    print("list=", tornado.options.options.list)
    app = tornado.web.Application([
        (r"/",IndexHandler)
    ])
    httpServer = tornado.httpserver.HTTPServer(app)
    httpServer.bind(tornado.options.options.port)
    httpServer.start(1)
    tornado.ioloop.IOLoop.current().start()

#E:\python-1705\day01\test>python36 server05.py
#http://localhost:7000/


