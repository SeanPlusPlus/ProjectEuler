#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from prime import is_prime, gen_primes 

# https://projecteuler.net/problem=60


def prime_pair(a, b):
    if not is_prime(int(a + b)):
        return False
    if not is_prime(int(b + a)):
        return False
    return True


def main():
    upperbound = 110
    primes = []
    for prime in gen_primes():
        if prime > upperbound:
            break
        primes.append(prime)

    pairs = {}
    for p in primes:
        for prime in primes:
            if p < prime:
                a = str(p)
                b = str(prime)
                if prime_pair(a, b):
                    try:
                        pairs[p].add(prime)
                    except KeyError:
                        pairs[p] = set()
                        pairs[p].add(prime)

    for k, v in pairs.items():
        print k, v
        for val in v:
            if val in pairs:
                i = set.intersection(v, pairs[val])
                if i:
                    print '*', k, val, i.pop()

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % "%.2f" % (time.time() - start_time))

    # seconds
