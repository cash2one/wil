#!/usr/bin/env python3

import io
import os

import tornado.ioloop
import tornado.web

class ImgHandler(tornado.web.RequestHandler):
    def get(self, dir):
        self.render("images.html", dir=dir, files=os.listdir(os.path.join("bmp", dir)))

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html", dirs=os.listdir("bmp"))

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
