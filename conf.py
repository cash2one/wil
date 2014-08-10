#!/usr/bin/env python3

human_steps = [
    (8, 4),  # idle
    (8, 6),  # walk
    (8, 6),  # run
    (1, 1),  # wait
    (8, 6),  # attack
    (8, 6),  # attack2
    (8, 8),  # attack3
    (8, 6),  # cast
    (2, 2),  # dig
    (8, 3),  # hurt
    (8, 4),  # die
]

HUMAN_DIRECTION = 8
BLEND_MODE_NORMAL = b'\x00'
BLEND_MODE_ADD = b'\x01'

nameit = "{}{:x}".format
def extract_human(i, n):
    mode = BLEND_MODE_NORMAL
    lst = []
    id = i//1200
    for _ in range(n):
        for j, k in human_steps:
            for d in range(HUMAN_DIRECTION):
                lst.append((i, i + k, nameit(id, d), mode))
                i += j
            id += 1
    return lst

bodies = extract_human(0, 12)
hairs = extract_human(1200, 4)
weapons = extract_human(1200, 60)

magics = [
    (0, 10, "hqs00", BLEND_MODE_ADD),
    (170, 180, "hqs20", BLEND_MODE_ADD),
] + [
    (i, i + 6, "hqs1{:x}".format((i - 10) // 10), BLEND_MODE_ADD)
    for i in range(10, 170, 10)
]

if __name__ == "__main__":
    print(len(bodies))
    print(len(hairs))
    print(len(weapons))
    print(weapons[-1])
    print(magics)
