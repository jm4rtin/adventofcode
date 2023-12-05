#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

def day2b(input):
    total = 0

    for line in input.split('\n'):
        if not len(line.strip()):
            continue

        sides = list(map(int, line.split('x')))
        sides.sort()
        total += (2 * sides[0]) + (2 * sides[1]) + (sides[0] * sides[1] * sides[2])

    print(total)

if __name__ == "__main__":
    day2b(open(sys.argv[1], 'r').read())
