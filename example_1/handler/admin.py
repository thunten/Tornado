#!/usr/bin/env python
# coding: utf-8
import tornado.web
import tornado.database

class loginHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("login")

class logoutHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("logout")

class indexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("admin - index")

handlers = [
    (r"/admin/", indexHandler),
    (r"/admin/login", loginHandler),
    (r"/admin/logout", logoutHandler),
]