#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

# https://projecteuler.net/problem=23

def getDivisors(n):    
    return set(reduce(list.__add__, 
        ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
    
def main():

    abundant = []
    nums = range(1,28123)
    for n in nums:
        divisors = getDivisors(n)
        divisors_sum = sum(list(divisors)) - n
        if divisors_sum > n:
            abundant.append(n)

    pairwise_sums = set()
    for num in abundant:
        for n in abundant:
            pairwise_sums.add(n + num)

    sum_not_abundant = 0
    for i, e in reversed(list(enumerate(nums))):
        if e not in pairwise_sums:
            sum_not_abundant += e

    print sum_not_abundant

if __name__ == '__main__':
    main()
