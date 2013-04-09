#!/usr/bin/env python
# coding: utf-8


#路由
from handler import admin
from handler import home
handlers = []
handlers.extend(admin.handlers)
handlers.extend(home.handlers)