#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

# https://projecteuler.net/problem=37

def trim_str(s, direction="left"):
    print s
    if direction == "left":
        trimmed = s[1:]
    else:
        trimmed = s[:-1]
    # check if int(trimmed) is prime, return False if not
    if len(trimmed) == 0:
        return True
    return trim_str(trimmed, direction)

def main():
    truncatable_primes = []
    s = "3797"
    trim_str(s)
    trim_str(s, direction="right")

if __name__ == '__main__':
    start_time = time.time()
    main()
    print("--- %s seconds ---" % "%.2f" % (time.time() - start_time) )

    # 6.12 seconds
