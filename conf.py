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
    (250, 260, "cs00", BLEND_MODE_ADD),
    (260, 270, "cs20", BLEND_MODE_ADD),
    (400, 410, "dhq00", BLEND_MODE_ADD),
    (570, 580, "dhq20", BLEND_MODE_ADD),
    (600, 610, "sds00", BLEND_MODE_ADD),
    (770, 780, "sds20", BLEND_MODE_ADD),
    (610, 620, "sds01", BLEND_MODE_ADD),
    (760, 770, "sds21", BLEND_MODE_ADD),
    (900, 906, "kjhh00", BLEND_MODE_ADD),
    (1140, 1150, "jgdy00", BLEND_MODE_ADD),
    (1360, 1370, "lhhh20", BLEND_MODE_ADD),
    (1320, 1335, "yld20", BLEND_MODE_ADD),
    (1340, 1355, "sszjs20", BLEND_MODE_ADD),
    (1380, 1390, "kmz00", BLEND_MODE_ADD),
    (1400, 1410, "kmz20", BLEND_MODE_ADD),
    (1390, 1400, "kmz21", BLEND_MODE_ADD),
    (1500, 1510, "zhkl00", BLEND_MODE_ADD),
    (1520, 1530, "yss00", BLEND_MODE_ADD),
    (1540, 1550, "jtyss20", BLEND_MODE_ADD),
    (1560, 1570, "yhzg00", BLEND_MODE_ADD),
    (1570, 1580, "yhzg20", BLEND_MODE_ADD),
    (1590, 1600, "sxyd00", BLEND_MODE_ADD),
    (1600, 1610, "sxyd20", BLEND_MODE_ADD),
    (1620, 1630, "hq00", BLEND_MODE_ADD),
    (1630, 1636, "hq20", BLEND_MODE_ADD),
    (1650, 1660, "blhy00", BLEND_MODE_ADD),
    (1660, 1680, "blhy20", BLEND_MODE_ADD),
    (1680, 1690, "dylg00", BLEND_MODE_ADD),
    (1790, 1800, "qtzls00", BLEND_MODE_ADD),
    (1800, 1810, "qtzls20", BLEND_MODE_ADD),
    (3840, 3850, "bpx00", BLEND_MODE_ADD),
    (3850, 3870, "bpx20", BLEND_MODE_ADD),
    (3880, 3890, "mfd00", BLEND_MODE_ADD),
    (3890, 3893, "mfd20", BLEND_MODE_ADD),
    (3900, 3903, "mfd21", BLEND_MODE_ADD),
    (3920, 3930, "sys00", BLEND_MODE_ADD),
    (3930, 3946, "sys20", BLEND_MODE_ADD),
    (3960, 3980, "xlqs00", BLEND_MODE_ADD),
    (3990, 4000, "xlqs20", BLEND_MODE_ADD),
] + [
    (i, i + 6, "hqs1{:x}".format((i - 10) // 10), BLEND_MODE_ADD)
    for i in range(10, 170, 10)
] + [
    (i, i + 6, "dhq1{:x}".format((i - 410) // 10), BLEND_MODE_ADD)
    for i in range(410, 570, 10)
] + [
    (i, i + 6, "jgdy1{:x}".format((i - 970) // 20), BLEND_MODE_ADD)
    for i in range(970, 1130, 20)
] + [
    (i, i + 3, "lhhh1{:x}".format((i - 1160) // 10), BLEND_MODE_NORMAL)
    for i in range(1160, 1320, 10)
]

if __name__ == "__main__":
    print(len(bodies))
    print(len(hairs))
    print(len(weapons))
    print(weapons[-1])
    print(magics)
