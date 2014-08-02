#!/usr/bin/env python3

import base64
import struct
import zlib

head_struct = struct.Struct(
    "<"       # little-endian
    "44s"     # title
    "i"       # image_count
    "i"       # color_count == 256
    "i"       # pallette_size == 256*4 == 1024
    "1024s"   # pallette
    )

assert head_struct.size == 1080


image_struct = struct.Struct(
    "<"       # little-endian
    "h"       # width
    "h"       # height
    "h"       # px
    "h"       # py
    )

assert image_struct.size == 8


bmp256_struct = struct.Struct(
    "<"       # little-endian
    "2s"      # "BM"
    "i"       # file_size = colors_pos + colors_size
    "4s"      # unknown
    "i"       # colors_pos == bmp256_struct.size == 1078
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
    tpl = list(bmp256_struct.unpack(f.read()))
