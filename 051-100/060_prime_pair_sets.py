#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import math
import sieve

# https://projecteuler.net/problem=60


def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))


def main():
    nums = [3, 7, 109, 673]
    for num in nums:
        compare = [x for x in nums if x != num]
        print num, compare
        for n in compare:
            concat_front = int(str(num) + str(n))
            concat_back = int(str(n) + str(num))
            print (is_prime(concat_front) and is_prime(concat_back)), \
                  concat_front, concat_back
    
    print nums, sum(nums)
    for p in sieve.gen_primes():
        print p


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % "%.2f" % (time.time() - start_time))

    # seconds
