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
    upperbound = 700
    primes = []
    for prime in gen_primes():
        if prime > upperbound:
            break
        primes.append(prime)

    pairs = set()
    for p in primes:
        for prime in primes:
            if p < prime:
                a = str(p)
                b = str(prime)
                if prime_pair(a, b):
                    pairs.add(a + ',' + b)

    print pairs

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % "%.2f" % (time.time() - start_time))

    # seconds
