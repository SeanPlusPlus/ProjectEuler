#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time 
from fractions import Fraction

# https://projecteuler.net/problem=57

def frac(i,f=(Fraction(1, 2))):
    if i == 2:
        return Fraction(1, (2 + f))
    i -= 1
    f = Fraction(1, (2 + f))
    return frac(i,f)

def main():
    i = 0
    for n in range(8,980):
        print n
        f = frac(n)
        li = str(sum((1,f))).split("/")
        if (len(li[0]) > len(li[1])):
            i += 1
        print "i", i

# the way i got the answer here is hacky
# if i run to 1K i get a recursion depth err
# but the pattern is that i will increment
# every 8, then every 8, then every 5
# and following that pattern from 980
# i could work backwards and see what 1K gives


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % "%.2f" % (time.time() - start_time) )
