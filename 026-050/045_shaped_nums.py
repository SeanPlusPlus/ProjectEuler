#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time, math, itertools

# https://projecteuler.net/problem=44

def triangular(n):
    return ((math.sqrt((8 * n) + 1) - 1) / 2).is_integer()

def pentagonal(n):
    return ((1 + math.sqrt((24 * n) + 1)) / 6).is_integer()

def hexagonal(n):
    return ((1 + math.sqrt(1 + (8 * n))) / 4).is_integer()

def junction():
    total = 3
    li = []
    nums = itertools.ifilter(triangular, itertools.count(1)) 
    for num in nums:
        print num

        if pentagonal(num):
            if hexagonal(num):
                li.append(num)

        if len(li) == total:
            return li 

def main():
    nums = junction()
    print nums
    
if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % "%.2f" % (time.time() - start_time) )

    # 559.13 seconds
    # sometimes it takes ten mins, such is life
