#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time, math, itertools

# https://projecteuler.net/problem=48


def prime_sieve(limit):
    a = [True] * limit 
    a[0] = a[1] = False
    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in xrange(i*i, limit, i):
                a[n] = False

def get_primes(limit):
    p = prime_sieve(limit)
    primes = []
    while True:
        try:
            prime = p.next()
            primes.append(prime)
        except StopIteration:
            return primes

def main():
    # limit = 1000 * 1000
    limit = 100
    primes = get_primes(limit)
    print primes

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % "%.2f" % (time.time() - start_time) )

    # 2.78 seconds
    # sometimes it takes ten mins, such is life
