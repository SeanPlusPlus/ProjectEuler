#!/usr/bin/env python
# -*- coding: utf-8 -*-

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

if __name__ == "__main__":
    main()
