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


def pairs(nums):
    for num in nums:
        compare = [x for x in nums if x != num]
        for n in compare:
            concat_front = int(num + n)
            concat_back = int(n + num)
            if not (is_prime(concat_front) and is_prime(concat_back)):
                return False
    
    return [int (n) for n in nums]


def main():
    for p in sieve.gen_primes():
        print p
        nums = [str(3), str(7) , str(109)]  # , 673] 
        p = str(p)
        if p not in nums:
            nums.append(p)
            ans = pairs(nums)
            if ans:
                print 'answer:', ans, sum(ans)
                return
    

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % "%.2f" % (time.time() - start_time))

    # seconds
