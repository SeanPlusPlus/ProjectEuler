#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from primes import get_primes

# https://projecteuler.net/problem=58


def northwest(first, last, li=[]):
    li = []
    a = 1
    for n in range(first, last):
        a = a + (n * 2)
        li.append(a)
    return li


def southeast(first, last, multiplier=[4, 4], li=[]):
    a = 1
    m = 0
    for n in range(first, last):
        try:
            m = multiplier.pop()
        except IndexError:
            multiplier = [m + 4, m + 4]
            m = multiplier.pop()
        a = a + m
        li.append(a)
    return li


def main():
    primes = get_primes(100)
    print primes
    first = 1
    last = 7
    top_right = northwest(first, last)
    bottom_left = southeast(first, last)
    nums = top_right + bottom_left
    print nums, len(top_right), len(bottom_left)
    p = len(set(primes).intersection(nums))
    n = len(nums) + 1
    print p, n
    print float(p) / float(n)


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % "%.2f" % (time.time() - start_time))
