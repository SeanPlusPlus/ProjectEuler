#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time, random
import itertools as it
from primes import get_primes

# https://projecteuler.net/problem=51
# 6 digit prime with exactly 3 repeating digits

def has_three_repeating_adjacent(s):
    indices = []
    s = str(s)
    for i in range(4):
        if s[i] == s[i+1] == s[i+2]:
            indices.append(i)
    return indices

def main():
    limit = 1000000
    primes = [p for p in get_primes(limit) if p > 99999]
    print "first prime:", primes[0], has_three_repeating_adjacent(primes[0])
    r = primes[random.randint(0,len(primes))]
    print "rand prime: ", r, has_three_repeating_adjacent(r)
    print "last prime: ", primes[-1], has_three_repeating_adjacent(primes[-1])
    print "total prime:", len(primes)





    # for prime in primes:
        # if has_three_repeating_adjacent(prime):
            # print prime

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % "%.2f" % (time.time() - start_time) )
