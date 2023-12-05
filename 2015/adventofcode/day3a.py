#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import collections

def day3a(input):
    houseCount = 1
    houses = collections.defaultdict(lambda: collections.defaultdict(int))
    x = 0
    y = 0

    houses[0][0] += 1

    for c in input:
        if c == '^':
            y -= 1
        elif c == 'v':
            y += 1
        elif c == '<':
            x -= 1
        elif c == '>':
            x += 1
        else:
            continue

        houses[x][y] += 1

        if houses[x][y] == 1:
            houseCount += 1

    print(houseCount)

if __name__ == "__main__":
    day3a(open(sys.argv[1], 'r').read())
