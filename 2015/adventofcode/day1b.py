#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

def day1b(input):
    floor = 0
    i = 1

    for c in input:
        if '(' == c:
            floor += 1
        elif ')' == c:
            floor -= 1

        if floor == -1:
            print(i)
            return

        i += 1

if __name__ == "__main__":
    day1b(open(sys.argv[1], 'r').read())
