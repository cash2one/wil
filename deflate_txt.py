#!/usr/bin/env python3

import struct
import sys

from lib import deflated_save


if __name__ == "__main__":
    fn = sys.argv[1]
    with open(fn, "rb") as f:
        s = f.read()
    deflated_save(struct.pack(">H", len(s)) + s, fn)
