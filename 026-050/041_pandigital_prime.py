#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

# https://projecteuler.net/problem=42

def primes_sieve2(limit):
    a = [True] * limit 
    a[0] = a[1] = False
    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in xrange(i*i, limit, i):
                a[n] = False

def is_pandigital(n):
    digits = str(n)
    digits_sorted= ''.join(sorted(digits))
    pan_digits = "".join([str(e) for e in range(1,len(digits)+1)])
    if pan_digits == digits_sorted:
        return True
    return False

def main():
    pan = []
    li = primes_sieve2(10000000)
    for el in li:
        if is_pandigital(el):
            pan.append(el)

    print max(pan)
    

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % "%.2f" % (time.time() - start_time) )

    # 11.20 seconds
