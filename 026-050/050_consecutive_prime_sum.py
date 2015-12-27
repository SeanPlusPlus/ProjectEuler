#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time, math, itertools

# https://projecteuler.net/problem=48

def prime_sieve(limit):
    a = [True] * limit 
    a[0] = a[1] = False
    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in xrange(i*i, limit, i):
                a[n] = False

def get_primes(limit):
    p = prime_sieve(limit)
    primes = []
    while True:
        try:
            prime = p.next()
            primes.append(prime)
        except StopIteration:
            return primes

def main():
    # limit = 1000
    limit = 1000000
    primes = get_primes(limit)
    primes_sum = [0]
    for i,p in enumerate(primes):
        ps = primes_sum[i] + p
        if ps > limit:
            break
        primes_sum.append(ps)
    primes_sum.pop(0)

    l = len(primes_sum)
    terms = 1
    for i,ps in enumerate(primes_sum):
        # i get this loop here: http://blog.dreamshire.com/project-euler-50-solution/
        for j in xrange(l-1, i+terms, -1):
                n = primes_sum[j] - primes_sum[i]
                if ((j - i > terms) and (n in primes)):
                    terms, max_prime = j-i, n
                    break
    print "terms", terms, "max_prime", max_prime

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % "%.2f" % (time.time() - start_time) )

    # 2.78 seconds
    # sometimes it takes ten mins, such is life
