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
def extract_s(i, n):
    lst = []
    id = 0
    for _ in range(n):
        for j, k in human_steps:
            for d in range(HUMAN_DIRECTION):
                lst.append((i, i + k, nameit(id, d)))
                i += j
            id += 1
    return lst

bodies = extract_s(0, 12)
hairs = extract_s(1200, 4)
weapons = extract_s(1200, 60)


if __name__ == "__main__":
    print(len(bodies))
    print(len(hairs))
    print(len(weapons))
    print(weapons[-1])
