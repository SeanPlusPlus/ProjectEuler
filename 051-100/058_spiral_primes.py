#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import itertools
from primes import get_primes

# https://projecteuler.net/problem=58


def northwest():
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
    primes = get_primes(1000)
    diag_primes = []
    diags = []
    nw = northwest()
    se = southeast()
    nw.next()  # this is number one, the start of spiral
    for i in itertools.count():

        nw_next = nw.next()

        # verify that highest num in spiral in primes set
        if not (nw_next < primes[-1]):
            print 'err need more primes'
            return

        se_next = se.next()

        # verify that highest num in spiral in primes set
        if not (se_next < primes[-1]):
            print 'err need more primes'
            return

        diags.append(nw_next)
        diags.append(se_next)
        print "nw.next()", nw_next
        print "se.next()", se_next

        if nw_next in primes:
            diag_primes.append(nw_next)
        if se_next in primes:
            diag_primes.append(se_next)

        if (i % 2) != 0:
            print diags  # a complete spiral
            print diag_primes  # set of primes in diags
            total_diags = float(len(diags) + 1)
            total_diag_primes = float(len(diag_primes))
            print total_diag_primes, "/", total_diags

        if len(diags) == 12:
            return


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % "%.2f" % (time.time() - start_time))
