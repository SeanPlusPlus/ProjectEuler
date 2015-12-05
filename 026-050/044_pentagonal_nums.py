#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time, math, itertools

# https://projecteuler.net/problem=44
# http://hubpages.com/education/How-to-Tell-If-a-Number-Is-a-Pentagonal-Number
# [1 + sqrt(24P + 1)]/6

def is_pentagonal(n):
    return ((1 + math.sqrt((24 * n) + 1)) / 6).is_integer()

def pentagonal(n):
    return int((n * ((3 * n) - 1)) / 2.0)

def pentagonal_series(limit):
    p = []
    n = 1
    while True:
        if n == limit:
            return p
        p.append(pentagonal(n))
        n += 1

def main():
    limit = 10000
    p = pentagonal_series(limit)
    for n in itertools.permutations(p,2):
        p_sum  = (n[0] + n[1])
        p_diff = (n[1] - n[0])
        if p_diff > 0:
            p_sum  = is_pentagonal(n[0] + n[1])
            p_diff = is_pentagonal(n[1] - n[0])
            if p_sum and p_diff:
                print n[1] - n[0] 
                return

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % "%.2f" % (time.time() - start_time) )

    # 56.58 seconds
