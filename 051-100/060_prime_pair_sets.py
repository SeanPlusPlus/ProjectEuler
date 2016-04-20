#!/usr/bin/env python
# -*- coding: utf-8 -*-

import itertools
import time
import math
import sieve

# https://projecteuler.net/problem=60


def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))


def prime_pair(li):
    concat_front = int(li[0] + li[1])
    concat_back = int(li[1] + li[0])
    if not (is_prime(concat_front) and is_prime(concat_back)):
        return False
    return ''.join(li)


def main():
    upperbound = 710
    primes = []
    for prime in sieve.gen_primes():
        primes.append(str(prime))
        if prime > upperbound:
            break

    perms = []
    for n in itertools.permutations(primes, 2):
        perms.append(n)

    pairs = {}
    for pair in perms:
        res = prime_pair(pair)
        if res and (''.join(list(reversed(pair))) not in pairs):
            pairs[res] = pair

    triples = []
    for k,v in pairs.items():
        for key, val in pairs.items():
            if (val[0] != v[0]) and (val[1] == v[1]):
                try:
                    match = pairs[ v[0] + val[0] ]
                    match = match + (val[1],)
                    triples.append(match)
                except KeyError:
                    pass

    quads = []
    for t in triples:
        print t
        for p in primes:
            if p not in t:
                if prime_pair([t[0], p]) and \
                        prime_pair([t[1], p]) and \
                        prime_pair([t[2], p]):
                    quads.append(t+ (p,))

    lowest = 10000000
    ans = None
    for q in quads:
        total = sum([int(n) for n in q])
        if total < lowest:
            lowest = total
            ans = q

    print ans, lowest

         

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % "%.2f" % (time.time() - start_time))

    # seconds
