#!/usr/bin/env python3

import array
import collections
import struct
import sys


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
mask_block = 0x8000

def get_map(map_file):
    with open(map_file, "rb") as f:
        data = f.read()
    W, H, reserved = struct_map_head.unpack(data[:struct_map_head.size])

    N = struct_map_tile.size
    cursor = struct_map_head.size

    assert len(data[cursor:]) == W * H * N, (W, H, len(data))

    map_struct = [[] for _ in range(H)]
    for w in range(W):
        for h in range(H):
            tile = struct_map_tile.unpack(data[cursor:cursor+N])
            map_struct[h].append(tile)
            cursor += N

    return map_struct


def print_map(m):
    mask = mask_block
    chars = [" ", "-", "|", "+"]
    for row in m:
        for t in row:
            id = bool(t[0] & mask) + bool(t[2] & mask) * 2
            print(chars[id], end="")
        print()


def map_mask(m):
    mask = mask_block
    arr = array.array("B", (
        bool(t[0] & mask) + (bool(t[2] & mask) << 1)
        for row in m
        for t in row
    ))
    return struct_w_h.pack(len(m[0]), len(m)) + arr.tobytes()


def map_ground(m):
    mask = mask_block - 1
    pack = struct.Struct(">H").pack
    lst = [t[0] & mask for row in m[::2] for t in row[::2]]
    return struct_w_h.pack(len(m[0]), len(m)) + b''.join(map(pack, lst))


def map_middle(m):
    w, h = len(m[0]), len(m)
    mask = mask_block - 1
    pack = struct.Struct(">IB").pack
    lst = [t[1] & mask for row in m for t in row]
    l = [pack(idx, i) for idx, i in enumerate(lst) if 0 < i < 255]
    #print(max(lst))
    #print(len(lst))
    #print(len(list(filter(None, lst))))
    return struct_w_h.pack(w, h) + b''.join(l)


def map_objects(m):
    w, h = len(m[0]), len(m)
    mask = mask_block - 1
    pack = struct.Struct(">IBH").pack
    lst = [(t[7], t[2] & mask) for row in m for t in row]
    l = [pack(idx, i, j) for idx, (i, j) in enumerate(lst) if j]
    return struct_w_h.pack(w, h) + b''.join(l)


def map_doors(m):
    "TODO"
    w, h = len(m[0]), len(m)
    mask = 0x7f
    pack = struct.Struct(">IBH").pack
    lst = [(t[3], t[4]) for row in m for t in row if t[4]]
    print(lst)

    lst = [(t[7], t[3] & mask) for row in m for t in row]
    l = [pack(idx, i, j) for idx, (i, j) in enumerate(lst) if 0 < j < 255]#todo
    return struct_w_h.pack(w, h) + b''.join(l)


def main():
    for fn in sys.argv[1:]:
        m = get_map(fn)
        with open('objects.bin', 'wb') as f:
            f.write(map_objects(m))
        with open('mask.bin', 'wb') as f:
            f.write(map_mask(m))
        with open('ground.bin', 'wb') as f:
            f.write(map_ground(m))
        with open('middle.bin', 'wb') as f:
            f.write(map_middle(m))


if __name__ == "__main__":
    main()
