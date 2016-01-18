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
    primes = get_primes(1000000)
    top_right = northwest()
    bottom_left = southeast()
    li = [top_right.next()]
    for n in itertools.count():
        li.append(top_right.next())
        li.append(bottom_left.next())
        if ((len(li) - 1) % 4) == 0:
            s = len(set(primes) & set(li))
            a = float(s) / float(len(li))
            l = (len(li) + 1) / 2
            print s, len(li), l
            if a < 0.5:
                return

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
