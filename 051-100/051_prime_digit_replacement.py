#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time, random
import itertools as it
from collections import Counter
from primes import get_primes

# https://projecteuler.net/problem=51
# 6 digit prime with exactly 3 repeating digits


def has_three_repeating_digits(s):
    indices = list(str(s))
    counts = dict(Counter(indices))
    for k, v in counts.iteritems():
        if v == 3:
            if int(k) < 3:
                return k
    return False


def main():
    limit = 1000000
    primes = [p for p in get_primes(limit) if p > 99999]
    r = primes[random.randint(0,len(primes))]

    for p in primes:
        n = has_three_repeating_digits(p)
        if n:
            li = [str(i) for i in range(int(n)+1, 10)]
            s = str(p)
            series = [p]
            for el in li:
                i = int(s.replace(n,el))
                if i in primes:
                    series.append(i)
            print p, "n:" + n, li, s, series
            if len(series) == 8:
                return


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % "%.2f" % (time.time() - start_time) )
