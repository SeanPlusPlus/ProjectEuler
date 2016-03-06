#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import itertools
import math

# https://projecteuler.net/problem=58


def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))


def northeast():
    li = []
    a = 1
    for i in itertools.count():
        a = a + (i * 2)
        yield a


def southeast():
    multiplier = [4, 4]
    a = 1
    m = 0
    for i in itertools.count():
        try:
            m = multiplier.pop()
        except IndexError:
            multiplier = [m + 4, m + 4]
            m = multiplier.pop()
        a = a + m
        yield a


def main():
    diag_primes = []
    diags = []
    ne = northeast()
    se = southeast()
    ne.next()  # the start of spiral
    ratio = 1  # prime ratio
    side_length = 1  # length of side of spiral
    for i in itertools.count():

        ne_next = ne.next()
        se_next = se.next()

        diags.append(ne_next)
        diags.append(se_next)

        if is_prime(ne_next):
            diag_primes.append(ne_next)
        if is_prime(se_next):
            diag_primes.append(se_next)

        if (i % 2) != 0:
            side_length += 2
            # print side_length, diags  # a complete spiral
            # print diag_primes  # set of primes in diags
            total_diags = float(len(diags) + 1)
            total_diag_primes = float(len(diag_primes))
            ratio = total_diag_primes / total_diags
            print side_length, total_diag_primes, "/", total_diags, "=", ratio

        if ratio < .1:
            return


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % "%.2f" % (time.time() - start_time))

    # 8.85 seconds
