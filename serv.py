#!/usr/bin/env python3

import io
import os

import tornado.ioloop
import tornado.web

class ImgHandler(tornado.web.RequestHandler):
    def get(self, dir):
        self.render("images.html", dir=dir, files=sorted(os.listdir(os.path.join("bmp", dir)[:1000])))

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html", dirs=sorted(os.listdir("bmp")[:1000]))

HANDLERS = [
    (r"/", MainHandler),
    (r"/(.+)", ImgHandler),
]

def run():
    io_loop = tornado.ioloop.IOLoop.instance()
    settings = {
        "static_path": "bmp",
        "template_path": "templates",
        "debug": False,
    }

    tornado.web.Application(
        HANDLERS, **settings).listen(1025)

    io_loop.start()


if __name__ == "__main__":
    run()
