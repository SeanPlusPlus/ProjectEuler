#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import math
from prime import is_prime, sieve

# https://projecteuler.net/problem=60


def prime_pair(li):
    concat_front = int(li[0] + li[1])
    concat_back = int(li[1] + li[0])
    if not (is_prime(concat_front) and is_prime(concat_back)):
        return False
    return True


def main():
    upperbound = 700
    di = {}
    li = []
    for prime in gen_primes():
        di[prime] = set()
        li.append(prime)
        if prime > upperbound:
            break

    for k, v in di.items():
        for el in li:
            if k < el:
                if prime_pair([str(k), str(el)]):
                    v.add(el)

    for k, v in di.items():
        if v:
            print k, v


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % "%.2f" % (time.time() - start_time))

    # seconds
