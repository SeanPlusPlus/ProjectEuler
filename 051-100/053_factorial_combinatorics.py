#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time, math

# https://projecteuler.net/problem=52
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def main():
    i = 7
    print factorial(i)

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % "%.2f" % (time.time() - start_time) )
    # 3.31 seconds
