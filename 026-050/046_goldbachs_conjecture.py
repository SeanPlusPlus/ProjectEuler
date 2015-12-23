#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pprint import pprint
import time, math

# https://projecteuler.net/problem=46
# got some help http://www.mathblog.dk/project-euler-46-odd-number-prime-square/

def primes_sieve(limit):
    a = [True] * limit 
    a[0] = a[1] = False
    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in xrange(i*i, limit, i):
                a[n] = False

def sum_ok(p, number):
    i = 0
    while True:
        i += 1
        if i > number:
            return False
        if (p + (2 * int(math.pow(i,2)))) == number:
            return True
    
def is_sum_of_prime_and_twice_square(number, primes):
    print number

    smaller_primes = []
    for p in primes:
        if p < number:
            smaller_primes.append(p)

    flag = True
    for p in smaller_primes:
        flag = sum_ok(p, number)
        if flag:
            break

    if not flag:
        print number
        return False

    return True


def main():
    primes = [p for p in primes_sieve(1000000)]
    notFound = True
    n = 3

    while True:
        if n not in primes:
            if not is_sum_of_prime_and_twice_square(n, primes):
                return
        n += 2
        

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % "%.2f" % (time.time() - start_time) )

    # 207.05 seconds
    # sometimes it takes ten mins, such is life
