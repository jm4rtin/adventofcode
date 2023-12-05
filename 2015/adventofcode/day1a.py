#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

def day1a(input):
    floor = 0

    for c in input:
        if '(' == c:
            floor += 1
        elif ')' == c:
            floor -= 1

    print(floor)

if __name__ == "__main__":
    day1a(open(sys.argv[1], 'r').read())
