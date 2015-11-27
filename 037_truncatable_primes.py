#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

# https://projecteuler.net/problem=37

def trim_left(s):
    print s
    trimmed = s[1:]
    if len(trimmed) == 0:
        return
    return trim_left(trimmed)

def trim_right(s):
    print s
    trimmed = s[:-1]
    if len(trimmed) == 0:
        return
    return trim_right(trimmed)

def main():
    s = "3797"
    trim_left(s)
    trim_right(s)

if __name__ == '__main__':
    start_time = time.time()
    main()
    print("--- %s seconds ---" % "%.2f" % (time.time() - start_time) )

    # 6.12 seconds
