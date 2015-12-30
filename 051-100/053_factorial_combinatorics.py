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
    li = []
    
    for n in range(11,101):
        for r in range(1,101):
            if r < n:
                i = factorial(n) / (factorial(r) * (factorial(n-r)))
                if (i > (1000 * 1000)):
                    li.append(i)

    print len(li)

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % "%.2f" % (time.time() - start_time) )
    # 3.31 seconds
