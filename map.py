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

def get_map(m):
    with open(m, "rb") as f:
        data = f.read()
    W, H, _ = struct_map_head.unpack(data[:struct_map_head.size])

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


def map_mask(m):
    mask = mask_block
    arr = array.array("B", (
        bool(t[0] & mask) + bool(t[2] & mask) * 2
        for row in m
        for t in row
    ))
    return struct_w_h.pack(len(m[0]), len(m)) + arr.tobytes()


def print_map(m):
    mask = mask_block
    chars = [" ", "-", "|", "+"]
    for row in m:
        for t in row:
            id = bool(t[0] & mask) + bool(t[2] & mask) * 2
            print(chars[id], end="")
        print()


def map_objects(m):
    mask = mask_block - 1
    pack = struct.Struct(">BH").pack
    return struct_w_h.pack(len(m[0]), len(m)) + b''.join(
        pack(t[-2], t[2] & mask)
        for row in m
        for t in row
    )


def map_middle(m):
    mask = mask_block - 1
    pack = struct.Struct(">H").pack
    return struct_w_h.pack(len(m[0]), len(m)) + b''.join(
        pack(t[1] & mask)
        for row in m
        for t in row
    )


def map_ground(m):
    mask = mask_block - 1
    pack = struct.Struct(">H").pack
    return struct_w_h.pack(len(m[0]), len(m)) + b''.join(
        pack(t[0] & mask)
        for row in m[::2]
        for t in row[::2]
    )


def main():
    for fn in sys.argv[1:]:
        m = get_map(fn)
        with open('mask.bin', 'wb') as f:
            f.write(map_mask(m))
        with open('ground.bin', 'wb') as f:
            f.write(map_ground(m))
        with open('middle.bin', 'wb') as f:
            f.write(map_middle(m))
        with open('objects.bin', 'wb') as f:
            f.write(map_objects(m))

if __name__ == "__main__":
    main()
