#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

# https://projecteuler.net/problem=27
# n² + an + b

ITER = 1001

# b is prime, so let's generate this set now
def get_prime_numbers():
    primes = []
    for num in range(3,ITER,2):
        if all(num%i!=0 for i in range(2,int(math.sqrt(num))+1)):
               primes.append(num)
    return set(primes)

# this is the series that walks through values of n, 
# terminating each time n is not a prime number
def prime_series(a, b, primes):
    for n in range(0,ITER):
        res = (n * n) + (a * n) + b
        prime = res in primes
        if not prime:
            return n 
    return n

def main():
    primes = get_prime_numbers()
    longest_consecutive = 0
    coefficients = []
    for a in range(0,ITER):

        # a is odd
        if a % 2 != 0:
            
            # b is prime
            for b in primes:

                # a nd b are positive
                consecutive = prime_series(a, b, primes)
                if consecutive > longest_consecutive:
                    longest_consecutive = consecutive
                    coefficients = a, b

                # a is negative and b is positive 
                consecutive = prime_series(-a, b, primes)
                if consecutive > longest_consecutive:
                    longest_consecutive = consecutive
                    coefficients = -a, b

                # b is negative and a is positive
                consecutive = prime_series(a, -b, primes)
                if consecutive > longest_consecutive:
                    longest_consecutive = consecutive
                    coefficients = a, -b

    print "longest consecutive", longest_consecutive
    print "coefficients", coefficients
    print "product of coefficients", coefficients[0] * coefficients[1]

if __name__ == '__main__':
    main()
