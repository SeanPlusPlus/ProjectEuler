#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time, math

# https://projecteuler.net/problem=48

def primes(n):
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)  
            n //= d
        d += 1
    if n > 1:
       primfac.append(n)
    return primfac

def main():
    target = 3
    previous = {}
    series = []
    n = 0
    while True:
        n += 1
        length = len(set(primes(n)))
        print n, length

        if length > target:
            if previous.get('length') == length:
                series.append(previous)
            else:
                series = []

        if len(series) == target:
            print series
            return

        previous = {
            "n": n,
            "length": length
        }


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % "%.2f" % (time.time() - start_time) )

    # 2.78 seconds
    # sometimes it takes ten mins, such is life
