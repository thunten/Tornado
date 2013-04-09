#!/usr/bin/env python
# coding: utf-8
import tornado.web

class indexHandler(tornado.web.RequestHandler):
    @property

    def db(self):
        return self.application.db

    def get(self):
        bookname = self.get_argument('bookname',"")
        sql = "select * from v2_leibie where 1=1 %s limit 20"
        conditions = " and name like '%%%%%s%%%%'" % bookname
        sql = sql % conditions
        try:
            entries = self.db.query(sql)
        except IOError:
            self.redirect('/index')
        else:
            self.render('index.html',entries=entries)

class listHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("list")

class viewHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("view")

handlers = [
    (r"/", indexHandler),
    (r"/list", listHandler),
    (r"/view", viewHandler),
]