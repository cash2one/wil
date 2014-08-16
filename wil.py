#!/usr/bin/env python3

import os
import os.path
import struct
import sys

import conf
from lib import *

def export(wil):
    assert wil.endswith(".wil")
    with open(wil, "rb") as f:
        wil_chunk = f.read()

    head = struct_head.unpack(wil_chunk[:struct_head.size])
    image_count = head[1]
    print(image_count, len(wil_chunk))

    pics = []

    pos = struct_head.size

    for i in range(image_count):
        pos_c = pos + struct_image.size
        w, h, x, y = struct_image.unpack(wil_chunk[pos:pos_c])
        pos += struct_image.size + w * h
        #print(i, len(wil_chunk[pos_c:pos_c + w * h]), w, h, x, y)
        if h > 1:
            assert w % 4 == 0, (i, w)
            pics.append((w, h, x, y, wil_chunk[pos_c:pos_c + w * h]))
        else:
            pics.append(None)

    return pics



def persist_to_bins(lst, dir, config=None):
    if not os.path.exists(dir):
        os.mkdir(dir)
    fmt_output = os.path.join(dir, "{}").format

    if config is None:
        for i, x in enumerate(lst):
            if x:
                w, h, x, y, colors = x
                deflated_save(pack_whxy(w, h, x, y) + colors, fmt_output(i))
    else:
        for begin, end, name in config:
            data = []
            for i in range(begin, end):
                w, h, x, y, colors = lst[i]
                data.append(pack_whxy(w, h, x, y))
                data.append(colors)
            deflated_save(b''.join(data), fmt_output(name))


def persist_to_single_bin(lst, fn):
    data = []
    for i in lst:
        if i is None:
            data.append(whxy_empty)
        else:
            w, h, x, y, colors = i
            data.append(pack_whxy(w, h, x, y))
            data.append(colors)
    deflated_save(b''.join(data), fn)


def persist_bmps(lst, dir):
    if not os.path.exists(dir):
        os.mkdir(dir)
    fmt_output = os.path.join(dir, "{}.bmp").format
    for i, args in enumerate(lst):
        if args:
            persist_bmp256(fmt_output(i), *args)


def persist_bmp256(fn, w, h, x, y, colors):
    tpl[BMP_W], tpl[BMP_H], tpl[BMP_CS] = w, h, w * h
    tpl[BMP_S] = struct_bmp256.size + tpl[BMP_CS]
    with open(fn, "wb") as f:
        f.write(struct_bmp256.pack(*tpl) + colors)



def main():
    for wil in sys.argv[1:]:
        persist_bmps(export(wil), os.path.join("bmp", os.path.basename(wil)[:-4]))

    return
    persist_to_bins(export("wil/Magic.wil"), "tmp/magics", conf.magics)
    persist_to_bins(export("wil/Magic2.wil"), "tmp/magics", conf.magics2)
    persist_to_bins(export("wil/Hum.wil"), "tmp/bodies", conf.bodies)
    persist_to_bins(export("wil/Hair.wil"), "tmp/hairs", conf.hairs)
    persist_to_bins(export("wil/Weapon.wil"), "tmp/weapons", conf.weapons)
    persist_to_single_bin(export("wil/DnItems.wil"), "tmp/items1")
    persist_to_single_bin(export("wil/Items.wil"), "tmp/items2")
    persist_to_single_bin(export("wil/StateItem.wil"), "tmp/items3")
    persist_to_single_bin(export("wil/MagIcon.wil"), "tmp/magic_icons")
    persist_to_bins(export("wil/mmap.wil"), "tmp/maps")
    persist_to_bins(export("wil/Tiles.wil"), "tmp/tiles")
    persist_to_bins(export("wil/SmTiles.wil"), "tmp/tilesm")
    persist_to_bins(filter(None, export("wil/Prguse.wil") + export("wil/Prguse2.wil")), "tmp/ui")
    persist_to_bins(export("wil/Objects.wil"), "tmp/objs0")
    persist_to_bins(export("wil/Objects2.wil"), "tmp/objs1")
    persist_to_bins(export("wil/Objects3.wil"), "tmp/objs2")
    persist_to_bins(export("wil/Objects4.wil"), "tmp/objs3")
    persist_to_bins(export("wil/Objects5.wil"), "tmp/objs4")
    persist_to_bins(export("wil/Objects6.wil"), "tmp/objs5")
    persist_to_bins(export("wil/Objects7.wil"), "tmp/objs6")


if __name__ == "__main__":
    main()
