#!/usr/bin/env python3

import struct
import zlib

struct_head = struct.Struct(
    "<"       # little-endian
    "44s"     # title
    "i"       # image_count
    "i"       # color_count == 256
    "i"       # pallette_size == 256*4 == 1024
    "1024s"   # pallette
    )

assert struct_head.size == 1080


struct_image = struct.Struct(
    "<"       # little-endian
    "h"       # width
    "h"       # height
    "h"       # px
    "h"       # py
    )

assert struct_image.size == 8


struct_bmp256 = struct.Struct(
    "<"       # little-endian
    "2s"      # "BM"
    "i"       # file_size = colors_pos + colors_size
    "4s"      # unknown
    "i"       # colors_pos == struct_bmp256.size == 1078
    "i"       # unknown == 40 ???
    "i"       # width
    "i"       # height
    "8s"      # unknown
    "i"       # colors_size == ((width + 3) // 4 * 4) * height
    "16s"     # unknown
    "1024s"   # pallette
    )

BMP_W = 5
BMP_H = 6
BMP_S = 1
BMP_CS = 8

with open("tpl_256", "rb") as f:
    tpl = list(struct_bmp256.unpack(f.read()))

pack_whxy = struct.Struct(">hhhh").pack
whxy_empty = pack_whxy(0,0,0,0)

def deflated_save(bin, fn):
    level = 1  # 1 is fastest, 9 is smallest
    with open(fn, "wb") as f:
        f.write(zlib.compress(bin, level)[2:-4])
