#!/usr/bin/env python
# -*- coding: utf-8 -*-

# https://projecteuler.net/problem=56

import time
import math


def sum_digits(n):
    i = 0
    for num in str(n):
        i += int(num)
    return i


def main():
    max_sum = 0
    for a in range(100):
        for b in range(100):
            i = sum_digits(a**b)
            if i > max_sum:
                max_sum = i
    print "max_sum", max_sum

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % "%.2f" % (time.time() - start_time))
