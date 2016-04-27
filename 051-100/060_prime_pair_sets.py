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
    return True


def main():
    upperbound = 700
    primes = []
    for prime in sieve.gen_primes():
        primes.append(str(prime))
        if prime > upperbound:
            break

    pairs = [] 
    for prime in primes:
        for p in primes:
            if prime_pair([prime, p]):
                li1 = [prime, p]                
                li2 = [p, prime]                
                if li1 and li2 not in pairs:
                    pairs.append(li1)
    
    for p in pairs:
        if '673' in p:
            print p

    print len(pairs)


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % "%.2f" % (time.time() - start_time))

    # seconds
