#!/usr/bin/env python3

monster_template_1 = [
    (0, 0, 8),  # idle
    (1, 64, 8),  # walk
    (2, 128, 8),  # attack
    (3, 192, 2),  # hurt
    (4, 208, 8),  # die
]

#e_attack 5
#e_die 6
#e_appear 7
#e_disappear 8

monster_template_2 = [
    (0, 0, 10),  # idle
    (1, 80, 10),  # walk
    (2, 160, 10),  # attack
    (3, 240, 2),  # hurt
    (4, 260, 10),  # die
]

monster_template_3 = [
    (2, 0, 10),  # attack
    (3, 80, 2),  # hurt
    (4, 100, 10),  # die
]

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

DIRECTIONS = 8


def render_monster(name, start, tpl, tpl_mask=(True, True, True, True, True, False, False, False)):
    lst = []
    for i, j, k in tpl:
        j += start
        for d in range(DIRECTIONS):
            if tpl_mask[i]:
                lst.append((j, j + k, "{}{}{:x}".format(name, i, d)))
            j += k
    return lst


def render_human(i, n):
    lst = []
    id = i//1200 * 22
    for _ in range(n):
        for j, k in human_steps:
            for d in range(DIRECTIONS):
                lst.append((i, i + k, "{}{:x}".format(id, d)))
                i += j
            id += 1
    return lst


bodies = render_human(0, 12)
hairs = render_human(1200, 4)
weapons = render_human(1200, 50)  # 50+ have problem

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


monsters = {
    "Mon1": (
        render_monster("g1", 0, monster_template_1, (1,1,1,0,0)) +
        render_monster("xr", 280, monster_template_1) +
        render_monster("g2", 560, monster_template_1, (1,0,1,0,0)) +
        render_monster("football", 840, monster_template_1, (1,1,0,0,0)) +
        []
    ),
    "Mon2": (
        render_monster("srh", 30, monster_template_3) +
        [
            (0, 10, "srh00"),
            (10, 20, "srh70"),
            (20, 30, "srh80"),
        ]
    ),
    "Mon3": (
        render_monster("kl1", 0, monster_template_2) +
        render_monster("kl2", 360, monster_template_2) +
        render_monster("kl3", 720, monster_template_2) +
        render_monster("kl4", 1080, monster_template_2) +
        render_monster("dq", 1440, monster_template_2) +
        render_monster("dgm", 1800, monster_template_2) +
        render_monster("dpm", 2160, monster_template_2) +
        render_monster("dcr", 2520, monster_template_2) +
        render_monster("dz", 2880, monster_template_2) +
        render_monster("sc", 3240, monster_template_2) +
        []
    ),
    "Mon4": (
        render_monster(40, 0, monster_template_2) +
        render_monster(41, 360, monster_template_2) +
        render_monster(42, 720, monster_template_2) +
        render_monster(43, 1080, monster_template_2) +
        render_monster(44, 1440, monster_template_2) +
        render_monster(46, 2160, monster_template_2) +
        render_monster(47, 2520, monster_template_2) +
        render_monster(48, 2880, monster_template_2) +
        render_monster(49, 3240, monster_template_2) +
        []
    ),
    "Mon5": (
        render_monster(50, 0, monster_template_2) +
        render_monster(51, 720, monster_template_2) +
        render_monster(52, 1080, monster_template_2) +
        render_monster(53, 1440, monster_template_2) +
        render_monster(54, 1800, monster_template_2) +
        render_monster(55, 2160, monster_template_2) +
        render_monster(57, 2520, monster_template_2) +
        render_monster(58, 2880, monster_template_2) +
        render_monster(59, 3240, monster_template_2) +
        []
    ),
    "Mon6": (
        render_monster(60, 0, monster_template_2) +
        render_monster(61, 430, monster_template_2) +
        render_monster(62, 860, monster_template_2) +
        render_monster(63, 1290, monster_template_2) +
        []
    ),
    "Mon7": (
        render_monster(70, 520, monster_template_2) +
        []
    ),
    "Mon15": [
        (0, 10, 11100),
        (10, 20, 11120),
        (50, 52, 11130),
        (60, 70, 11140),
        (100, 110, 11150),
        (70, 80, 11170),
        (80, 90, 11180),
    ],
    "Mon17": (
        render_monster(0, 0, monster_template_2) +
        render_monster(1, 360, monster_template_2) +
        []
    ),
}

if __name__ == "__main__":
    print(monsters["Mon17"])
    print(len(bodies))
    print(len(hairs))
    print(len(weapons))
    print(weapons[-1])
    print(magics)
