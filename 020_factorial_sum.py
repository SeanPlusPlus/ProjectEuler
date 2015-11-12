#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

# https://projecteuler.net/problem=20

def main():
    nums = str(math.factorial(100))
    ans = 0
    for char in nums:
        ans += int(char)

    print ans

if __name__ == '__main__':
    main()
