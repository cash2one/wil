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
                lst.append((list(range(i, i + k)), "{}{}{:x}".format(name, i, d)))
            j += k
    return lst


def render_human(i, n):
    lst = []
    id = i//1200 * 22
    for _ in range(n):
        for j, k in human_steps:
            for d in range(DIRECTIONS):
                lst.append((list(range(i, i + k)), "{}{:x}".format(id, d)))
                i += j
            id += 1
    return lst


bodies = render_human(0, 12)
hairs = render_human(1200, 4)
weapons = render_human(1200, 50)  # 50+ have problem

magics = [
    (0, 10, "20100"),
    (170, 178, "20120"),
    (200, 210, "30100"),
    (370, 380, "30120"),
    (250, 260, "teleport00"),
    (260, 270, "teleport20"),
    (400, 410, "20700"),
    (570, 580, "20720"),
    (600, 610, "30300"),
    (770, 780, "30320"),
    (610, 620, "30301"),
    (760, 770, "30321"),
    (900, 906, "20200"),
    (1140, 1150, "21000"),
    (1360, 1370, "30420"),
    (1320, 1335, "30820"),
    (1340, 1355, "30920"),
    (1380, 1390, "31100"),
    (1400, 1410, "31120"),
    (1390, 1400, "31121"),
    (1500, 1510, "30500"),
    (1520, 1530, "30600"),
    (1540, 1550, "30720"),
    (1560, 1570, "20300"),
    (1570, 1580, "20320"),
    (1590, 1600, "20600"),
    (1600, 1610, "20620"),
    (1620, 1630, "20900"),
    (1630, 1636, "20920"),
    (1650, 1660, "20800"),
    (1660, 1680, "20820"),
    (1680, 1690, "21100"),
    (1790, 1800, "31100"),
    (1800, 1810, "31120"),
    (3840, 3850, "21400"),
    (3850, 3870, "21420"),
    (3880, 3890, "21200"),
    (3890, 3893, "21220"),
    (3900, 3903, "21221"),
    (3920, 3930, "21300"),
    (3930, 3946, "21320"),
    (3960, 3980, "31000"),
    (3990, 4000, "31020"),
] + [
    (i, i + 6, "2011{:x}".format((i - 10) // 10))
    for i in range(10, 170, 10)
] + [
    (i, i + 6, "2071{:x}".format((i - 410) // 10))
    for i in range(410, 570, 10)
] + [
    (i, i + 6, "2101{:x}".format((i - 970) // 20))
    for i in range(970, 1130, 20)
] + [
    (i, i + 3, "3041{:x}".format((i - 1160) // 10))
    for i in range(1160, 1320, 10)
]

magics2 = [
    (0, 10, "31300"),
    (20, 23, "20500"),
    (10, 15, "20520"),
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
