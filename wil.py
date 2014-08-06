#!/usr/bin/env python3

import os
import os.path
import struct

from lib import *

def export(wil):
    assert wil.endswith(".wil")
    with open(wil, "rb") as f:
        wil_chunk = f.read()

    head = head_struct.unpack(wil_chunk[:head_struct.size])
    image_count = head[1]
    print(image_count, len(wil_chunk))

    pics = []

    pos = head_struct.size

    for i in range(image_count):
        pos_c = pos + image_struct.size
        w, h, x, y = image_struct.unpack(wil_chunk[pos:pos_c])
        pos += image_struct.size + w * h
        #print(i, len(wil_chunk[pos_c:pos_c + w * h]), w, h, x, y)
        if h > 1:
            assert w % 4 == 0, (i, w)
            pics.append((w, h, x, y, wil_chunk[pos_c:pos_c + w * h]))
        else:
            pics.append(None)

    return pics



def persist_to_bins(lst, dir, conf):
    if not os.path.exists(dir):
        os.mkdir(dir)
    fmt_output = os.path.join(dir, "{}").format
    for begin, end, name in conf:
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
    tpl[BMP_S] = bmp256_struct.size + tpl[BMP_CS]
    with open(fn, "wb") as f:
        f.write(bmp256_struct.pack(*tpl) + colors)



if __name__ == "__main__":
    import sys
    for wil in sys.argv[1:]:
        persist_bmps(export(wil), os.path.join("bmp", os.path.basename(wil)[:-4]))

    import conf
    persist_to_bins(export("../wil_files/Hum.wil"), "tmp/bodies", conf.bodies)
    persist_to_bins(export("../wil_files/Hair.wil"), "tmp/hairs", conf.hairs)
    persist_to_bins(export("../wil_files/Weapon.wil"), "tmp/weapons", conf.weapons)
    persist_to_single_bin(export("../wil_files/DnItems.wil"), "tmp/items1")
    persist_to_single_bin(export("../wil_files/Items.wil"), "tmp/items2")
    persist_to_single_bin(export("../wil_files/StateItem.wil"), "tmp/items3")
    persist_to_single_bin(export("../wil_files/MagIcon.wil"), "tmp/magic_icons")
    persist_to_single_bin(export("../wil_files/Prguse.wil"), "tmp/ui")
