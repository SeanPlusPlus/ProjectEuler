#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from primes import get_primes

# https://projecteuler.net/problem=58


def northwest():
    li = []
    a = 1
    for n in range(1, 7):
        a = a + (n * 2)
        li.append(a)
    return li


def southeast():
    return []


def main():
    primes = get_primes(10)
    print primes
    print northwest()
    print southeast()


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % "%.2f" % (time.time() - start_time))
