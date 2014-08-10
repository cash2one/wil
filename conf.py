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
    (200, 210, "zys00", BLEND_MODE_ADD),
    (370, 380, "zys20", BLEND_MODE_ADD),
    (250, 260, "sxyd00", BLEND_MODE_ADD),
    (260, 270, "sxyd20", BLEND_MODE_ADD),
    (400, 410, "dhq00", BLEND_MODE_ADD),
    (570, 580, "dhq20", BLEND_MODE_ADD),
    (600, 610, "sds00", BLEND_MODE_ADD),
    (770, 780, "sds20", BLEND_MODE_ADD),
    (610, 620, "sds01", BLEND_MODE_ADD),
    (760, 770, "sds21", BLEND_MODE_ADD),
    (900, 906, "kjhh00", BLEND_MODE_ADD),
] + [
    (i, i + 6, "hqs1{:x}".format((i - 10) // 10), BLEND_MODE_ADD)
    for i in range(10, 170, 10)
] + [
    (i, i + 6, "dhq1{:x}".format((i - 410) // 10), BLEND_MODE_ADD)
    for i in range(410, 570, 10)
] + [
    (i, i + 6, "jgdy1{:x}".format((i - 970) // 20), BLEND_MODE_ADD)
    for i in range(970, 1130, 20)
]

if __name__ == "__main__":
    print(len(bodies))
    print(len(hairs))
    print(len(weapons))
    print(weapons[-1])
    print(magics)
