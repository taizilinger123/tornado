#!/usr/bin/env python
# -*- coding:utf-8 -*-
import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options
# from tornado.options import options,define

# 定义两个参数
tornado.options.define("port",default=8000,type=int)
tornado.options.define("list",default=[],type=str,multiple=True)

class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write("sunck is a good man")

if __name__ == "__main__":
    # 转换命令行参数,并保存到tornado.options.options
    tornado.options.parse_command_line()
    print("list=", tornado.options.options.list)
    app = tornado.web.Application([
        (r"/",IndexHandler)
    ])
    httpServer = tornado.httpserver.HTTPServer(app)
    # 使用变量的值
    httpServer.bind(tornado.options.options.port)
    httpServer.start(1)
    tornado.ioloop.IOLoop.current().start()

#python36 server04.py --port=9000 --list=good,nice,handsome,cool
#http://localhost:9000/

