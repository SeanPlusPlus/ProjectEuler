#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

# https://projecteuler.net/problem=27
# n² + an + b

ITER = 1001

def get_prime_numbers():
    primes = []
    for num in range(3,ITER,2):
        if all(num%i!=0 for i in range(2,int(math.sqrt(num))+1)):
               primes.append(num)
    return primes

def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    try:
        return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))
    except ValueError:
        return False

def prime_series(a,b):

    for n in range(0,ITER):
        res = (n * n) + (a * n) + b
        prime = is_prime(res)
        print "n", n, "prime", prime, "res", res
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

                consecutive = prime_series(a, b)
                if consecutive > longest_consecutive:
                    longest_consecutive = consecutive
                    coefficients = a, b
                print "a", "b", a, b, "consecutive", consecutive, "\n"

                consecutive = prime_series(-a, b)
                if consecutive > longest_consecutive:
                    longest_consecutive = consecutive
                    coefficients = -a, b
                print "-a", "b", -a, b, "consecutive", consecutive, "\n"

                consecutive = prime_series(a, -b)
                if consecutive > longest_consecutive:
                    longest_consecutive = consecutive
                    coefficients = a, -b
                print "a", "-b", a, -b, "consecutive", consecutive, "\n"

    print "longest consecutive", longest_consecutive
    print "coefficients", coefficients
    print "product of coefficients", coefficients[0] * coefficients[1]

if __name__ == '__main__':
    main()
