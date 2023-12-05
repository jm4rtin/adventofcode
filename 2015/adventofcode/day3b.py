#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import collections

def day3b(input):
    houseCount = 1
    houses = collections.defaultdict(lambda: collections.defaultdict(int))
    person = 0
    x = [0, 0]
    y = [0, 0]

    houses[0][0] += 2

    for c in input:
        if c == '^':
            y[person] -= 1
        elif c == 'v':
            y[person] += 1
        elif c == '<':
            x[person] -= 1
        elif c == '>':
            x[person] += 1
        else:
            continue

        houses[ x[person] ][ y[person] ] += 1

        if houses[ x[person] ][ y[person] ] == 1:
            houseCount += 1

        person = (person + 1) % 2

    print(houseCount)

if __name__ == "__main__":
    day3b(open(sys.argv[1], 'r').read())
