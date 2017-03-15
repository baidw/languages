#!/usr/bin/env python
# -*- coding:utf-8 -*-
import web

urls = (
    '/', 'index'
)


class index:

    def GET(self):
        return "Hello,python web.py world!"


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()

# python python_web.py 8090
# 通过PC客户端浏览器访问http://localhost:8090/ 查看效果
