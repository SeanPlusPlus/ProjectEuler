#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time, math, itertools

# https://projecteuler.net/problem=48


def get_primes(limit):
    a = [True] * limit 
    a[0] = a[1] = False
    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in xrange(i*i, limit, i):
                a[n] = False

def main():
    # limit = 1000 * 1000
    limit = 100
    p = get_primes(limit)
    while True:
        try:
            prime = p.next()
            print prime
        except StopIteration:
            return

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % "%.2f" % (time.time() - start_time) )

    # 2.78 seconds
    # sometimes it takes ten mins, such is life
