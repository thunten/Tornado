#!/usr/bin/env python
# coding: utf-8
import os.path
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import ConfigParser

from tornado.options import define, options

define("port", default=8888, help="run on the given port", type=int)

class HelloModule(tornado.web.UIModule):
    def render(self):
        return '<h1>Hello, world!</h1>'

class Application(tornado.web.Application):
    def __init__(self):
        #导入路由规则
        from config import urls
        #站点配置
        settings = {
            'debug': False,
            'gzip': True,
            'cookie_secret' : '"61o42QsKXQAGaYdvfasky5aDfpsu$^EQnp2XdTP1o/Vo+', #请修改随机值
            'root_path' : os.path.dirname(__file__),
            'template_path' : os.path.join(os.path.dirname(__file__), "templates"),
            'static_path' : os.path.join(os.path.dirname(__file__), "static"),
        }
        ui_modules={'Hello', HelloModule}
        tornado.web.Application.__init__(self, urls.handlers, **settings)
        #导入数据库配置
        web_config = ConfigParser.RawConfigParser()
        web_config.read('config/web.ini')
        host = web_config.get('main.database', 'host')
        port = web_config.get('main.database', 'port')
        database = web_config.get('main.database', 'databasename')
        user = web_config.get('main.database', 'username')
        password = web_config.get('main.database', 'password')        
        #连接数据库
        self.db = tornado.database.Connection(host,database,user,password)

def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()