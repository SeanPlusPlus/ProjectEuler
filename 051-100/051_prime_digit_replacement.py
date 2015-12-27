#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from primes import get_primes

# https://projecteuler.net/problem=51


def main():
    limit = 1000
    primes = get_primes(limit)
    for p in primes:
        print p

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % "%.2f" % (time.time() - start_time) )

    # 2.78 seconds
    # sometimes it takes ten mins, such is life
