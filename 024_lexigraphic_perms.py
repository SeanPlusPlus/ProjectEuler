#!/usr/bin/env python
# -*- coding: utf-8 -*-

import itertools

# https://projecteuler.net/problem=24

def main():

    total = 1000000
    count = 0
    nums  = range(0,10)

    iterable = itertools.permutations(nums)
    for i in iterable:
        count += 1
        if count == total:
            print str(i).replace(', ', '') 
            return

if __name__ == '__main__':
    main()
