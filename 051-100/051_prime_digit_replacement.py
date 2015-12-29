#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import itertools as it
from primes import get_primes

# https://projecteuler.net/problem=51

def main():
    limit = 100000
    primes = get_primes(limit)
    print "last prime", primes[-1]

    series = []
    for n in xrange(10):
        s = str(n)
        i = "56" + s + s + "3"
        if int(i) in primes:
            series.append(i)

    print len(series), series 

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % "%.2f" % (time.time() - start_time) )
