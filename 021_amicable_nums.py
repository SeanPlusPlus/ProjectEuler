#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

# https://projecteuler.net/problem=21

def getDivisors(n):

    divisors = []
    for num in range(1, int(math.sqrt(n)) + 1):
        if (n % num) == 0:
            divisors.append(num)
            divisors.append(n/num)
    return divisors

def main():

    amicable_sum = 0
    for target in range(1,10000):

        divisors = getDivisors(target)
        output_a = (sum(divisors) - target)

        # no perfect numbers!
        if output_a == target:
            continue

        if math.sqrt(target).is_integer():
            output_a = (output_a - int(math.sqrt(target)))

        divisors = getDivisors(output_a)
        output_b = (sum(divisors) - output_a)

        if math.sqrt(output_a).is_integer():
            output_b = (output_b - int(math.sqrt(output_a)))

        if output_b == target:
            print target
            amicable_sum += target

    print amicable_sum

if __name__ == '__main__':
    main()
