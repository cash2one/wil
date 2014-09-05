#!/usr/bin/env python3

import array
import collections
import pprint
import json
import struct
import sys
import os
import os.path


struct_map_head = struct.Struct(
    "<"       # little-endian
    "H"       # width
    "H"       # height
    "48s"     # reserved
)

struct_map_tile = struct.Struct(
    "<"       # little-endian
    "H"       # backgound
    "H"       # middle
    "H"       # object
    "B"       # door index
    "B"       # door offset
    "B"       # animation frames
    "B"       # animation tick
    "B"       # objects file index
    "B"       # light
)

struct_w_h = struct.Struct(">HH")
mask_short = 0x7fff
mask_byte = 0x7f

def get_map(map_file):
    with open(map_file, "rb") as f:
        data = f.read()
    W, H, reserved = struct_map_head.unpack(data[:struct_map_head.size])

    N = struct_map_tile.size
    cursor = struct_map_head.size

    assert len(data[cursor:]) >= W * H * N, (W, H, N, len(data))

    map_struct = [[] for _ in range(H)]
    for w in range(W):
        for h in range(H):
            tile = struct_map_tile.unpack(data[cursor:cursor+N])
            map_struct[h].append(tile)
            cursor += N

    return map_struct


def print_map(m):
    mask = mask_short + 1
    chars = [" ", "-", "|", "+"]
    for row in m:
        for t in row:
            id = bool(t[0] & mask) + bool(t[2] & mask) * 2
            print(chars[id], end="")
        print()


def map_mask(m):
    mask = mask_short + 1
    arr = array.array("B", (
        bool(t[0] & mask) + (bool(t[2] & mask) << 1)
        for row in m
        for t in row
    ))
    return struct_w_h.pack(len(m[0]), len(m)) + arr.tobytes()


def map_ground(m):
    pack = struct.Struct(">H").pack
    lst = [t[0] & mask_short for row in m[::2] for t in row[::2]]
    return struct_w_h.pack(len(m[0]), len(m)) + b''.join(map(pack, lst))


def map_middle(m):
    w, h = len(m[0]), len(m)
    pack = struct.Struct(">IB").pack
    lst = [t[1] & mask_short for row in m for t in row]
    l = [pack(idx, i) for idx, i in enumerate(lst) if 0 < i < 255]
    #print(max(lst))
    #print(len(lst))
    #print(len(list(filter(None, lst))))
    return struct_w_h.pack(w, h) + b''.join(l)


def map_objects(m):
    w, h = len(m[0]), len(m)
    pack = struct.Struct(">IBH").pack
    lst = [(t[7], t[2] & mask_short, t[5]) for row in m for t in row]
    l = [pack(idx, i, j) for idx, (i, j, ani) in enumerate(lst) if j and i < 32 and not ani]
    return struct_w_h.pack(w, h) + b''.join(l)


anis = set()
def map_animations(m):
    w, h = len(m[0]), len(m)
    mask1 = mask_byte + 1
    lst = [(t[7], t[2] & mask_short, t[5]) for row in m for t in row]
    #l = [(i, j, ani & mask_byte, bool(ani & mask1)) for idx, (i, j, ani) in enumerate(lst) if j > 16 and i < 32 and ani]
    #pprint.pprint(set(l))
    #anis.update(l)
    d = {idx: (i, j, ani & mask_byte, bool(ani & mask1)) for idx, (i, j, ani) in enumerate(lst) if j > 16 and i < 32 and ani}
    d["w"], d["h"] = w, h
    return json.dumps(d, separators=(",", ":"))


def map_doors(m):
    "TODO"
    w, h = len(m[0]), len(m)
    pack = struct.Struct(">IBH").pack

    lst = [(t[7], t[2]&0x7fff, t[3], t[4]&0xff) for row in m for t in row if t[4]]
    print(lst)


def convert(map_file):
    name = os.path.join("tmp", "map", os.path.basename(os.path.splitext(map_file)[0]))
    print(name)
    m = get_map(map_file)
    with open(name + ".animations", "w") as f:
        f.write(map_animations(m))
    with open(name + ".objects", "wb") as f:
        f.write(map_objects(m))
    with open(name + ".mask", "wb") as f:
        f.write(map_mask(m))
    with open(name + ".ground", "wb") as f:
        f.write(map_ground(m))
    with open(name + ".middle", "wb") as f:
        f.write(map_middle(m))


def main():
    for fn in sys.argv[1:]:
        convert(fn)


if __name__ == "__main__":
    main()
    #pprint.pprint(anis)
