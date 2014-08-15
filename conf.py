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

nameit = "{}{:x}".format
def extract_human(i, n):
    lst = []
    id = i//1200 * 22
    for _ in range(n):
        for j, k in human_steps:
            for d in range(HUMAN_DIRECTION):
                lst.append((i, i + k, nameit(id, d)))
                i += j
            id += 1
    return lst

bodies = extract_human(0, 12)
hairs = extract_human(1200, 4)
weapons = extract_human(1200, 50)  # 50+ have problem

magics = [
    (0, 10, "hqs00"),
    (170, 180, "hqs20"),
    (200, 210, "zys00"),
    (370, 380, "zys20"),
    (250, 260, "cs00"),
    (260, 270, "cs20"),
    (400, 410, "dhq00"),
    (570, 580, "dhq20"),
    (600, 610, "sds00"),
    (770, 780, "sds20"),
    (610, 620, "sds01"),
    (760, 770, "sds21"),
    (900, 906, "kjhh00"),
    (1140, 1150, "jgdy00"),
    (1360, 1370, "lhhh20"),
    (1320, 1335, "yld20"),
    (1340, 1355, "sszjs20"),
    (1380, 1390, "kmz00"),
    (1400, 1410, "kmz20"),
    (1390, 1400, "kmz21"),
    (1500, 1510, "zhkl00"),
    (1520, 1530, "yss00"),
    (1540, 1550, "jtyss20"),
    (1560, 1570, "yhzg00"),
    (1570, 1580, "yhzg20"),
    (1590, 1600, "sxyd00"),
    (1600, 1610, "sxyd20"),
    (1620, 1630, "hq00"),
    (1630, 1636, "hq20"),
    (1650, 1660, "blhy00"),
    (1660, 1680, "blhy20"),
    (1680, 1690, "dylg00"),
    (1790, 1800, "qtzls00"),
    (1800, 1810, "qtzls20"),
    (3840, 3850, "bpx00"),
    (3850, 3870, "bpx20"),
    (3880, 3890, "mfd00"),
    (3890, 3893, "mfd20"),
    (3900, 3903, "mfd21"),
    (3920, 3930, "sys00"),
    (3930, 3946, "sys20"),
    (3960, 3980, "xlqs00"),
    (3990, 4000, "xlqs20"),
] + [
    (i, i + 6, "hqs1{:x}".format((i - 10) // 10))
    for i in range(10, 170, 10)
] + [
    (i, i + 6, "dhq1{:x}".format((i - 410) // 10))
    for i in range(410, 570, 10)
] + [
    (i, i + 6, "jgdy1{:x}".format((i - 970) // 20))
    for i in range(970, 1130, 20)
] + [
    (i, i + 3, "lhhh1{:x}".format((i - 1160) // 10))
    for i in range(1160, 1320, 10)
]

magics2 = [
    (0, 10, "zhss00"),
    (20, 23, "lds00"),
    (10, 15, "lds20"),
]

if __name__ == "__main__":
    print(len(bodies))
    print(len(hairs))
    print(len(weapons))
    print(weapons[-1])
    print(magics)
