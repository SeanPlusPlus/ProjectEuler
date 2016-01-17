#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import itertools
from primes import get_primes

# https://projecteuler.net/problem=58


def northwest():
    li = []
    a = 1
    for i in itertools.count():
        a = a + (i * 2)
        yield a


def southeast():
    multiplier = [4, 4]
    a = 1
    m = 0
    for i in itertools.count():
        try:
            m = multiplier.pop()
        except IndexError:
            multiplier = [m + 4, m + 4]
            m = multiplier.pop()
        a = a + m
        yield a


def main():
    primes = get_primes(100)
    top_right = northwest()
    bottom_left = southeast()
    li = []
    for n in range(6):
        li.append(top_right.next())
        li.append(bottom_left.next())
    li.append(top_right.next())
    print primes
    print li, len(set(primes) & set(li)), len(li)
    print float(len(set(primes) & set(li))) / float(len(li))

    # nums = top_right + bottom_left
    # print nums, len(top_right), len(bottom_left)
    # p = len(set(primes).intersection(nums))
    # n = len(nums) + 1
    # print p, n
    # print float(p) / float(n)


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % "%.2f" % (time.time() - start_time))
