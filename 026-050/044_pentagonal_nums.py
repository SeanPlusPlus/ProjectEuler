#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time 

# https://projecteuler.net/problem=44

def pentagonal(n):
    return int((n * ((3 * n) - 1)) / 2.0)

def main():

    p = [pentagonal(n) for n in range(1,11)]
    print p

    j = 4
    k = 7

    p_sum = ((p[j-1] + p[k-1]) in p)
    p_diff = ((p[k-1] - p[j-1]) in p)

    print p_sum, p_diff

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % "%.2f" % (time.time() - start_time) )

    # 102.81 seconds
