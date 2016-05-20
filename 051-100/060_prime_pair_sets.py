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


def prime_set(li, prime):
    for p in li:
        a = str(p)
        b = str(prime)
        if not prime_pair(a, b):
            return False
    return li + [prime]


def main():
    upperbound = 10000
    primes = []
    for prime in gen_primes():
        if prime > upperbound:
            break
        primes.append(prime)

    print 'pairs'

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

    print 'triples'

    triples = []
    for k, v in pairs.items():
        for val in v:
            if val in pairs:
                intersect = set.intersection(v, pairs[val])
                if intersect:
                    i = intersect.pop()
                    triples.append([k, val, i])

    print 'quads'

    quads = []
    for t in triples:
        for prime in primes:
            s = prime_set(t, prime)
            if s:
                quads.append(s)

    print 'pents'

    pents = []
    for q in quads:
        for prime in primes:
            s = prime_set(q, prime)
            if s:
                pents.append(s)

    lowest = 1000000000
    for p in pents:
        res = sum(p)
        if res < lowest:
            lowest = res

    print lowest



            
        

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % "%.2f" % (time.time() - start_time))

    # 587 seconds
