#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import math

# https://projecteuler.net/problem=35

ITER = 1000001
#ITER = 101

def get_prime_numbers():
    primes = [2]
    for num in range(3,ITER,2):
        if all(num%i!=0 for i in range(2,int(math.sqrt(num))+1)):
               primes.append(num)
    return primes

def digitList(i):
    return [int(el) for el in list(str(i))]

def numFromList(li):
    i = 0
    i += int(''.join(str(e) for e in li))
    return i

def permutationsOkay(li, primes):
    n = len(li)
    for el in [[li[i - j] for i in range(n)] for j in range(n)]:
        num = numFromList(el)
        if num not in primes:
            return False
    return True

def main():
    is_circular = 0
    primes = get_prime_numbers()
    for p in primes:
        li = digitList(p)
        if permutationsOkay(li, primes):
            is_circular += 1
            print p, li 

    print "is_circular: ", is_circular

if __name__ == '__main__':
    start_time = time.time()
    main()
    print("--- %s seconds ---" % "%.2f" % (time.time() - start_time) )

    # 290.45 seconds
