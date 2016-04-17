#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import math

# https://projecteuler.net/problem=60


def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))


def main():
    nums = [3, 7, 109, 673]
    for n in nums:
        print is_prime(n)



if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % "%.2f" % (time.time() - start_time))

    # seconds
