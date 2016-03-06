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
    # primes = get_primes(10000000)
    diags = []
    threshold = 5  # must be odd to complete one wrap of square
    nw = northwest()
    se = southeast()
    nw.next()  # this is number one, the start of spiral
    for i in itertools.count():
        nw_next = nw.next()
        se_next = se.next()
        diags.append(nw_next)
        diags.append(se_next)
        print "nw.next()", nw_next
        print "se.next()", se_next
        if (i % 2) != 0:
            # this is a complete spiral
            print diags
        if i == threshold:
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
