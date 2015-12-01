#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

# https://projecteuler.net/problem=30

def main():
    ITER = 1000000
    exp =  5
    total = 0
    for i in range(2, ITER):
        i_sum = 0
        for c in list(str(i)):
            i_sum += pow( int(c), exp)
        if i == i_sum:
            print [c for c in list(str(i))], [pow (int(c), exp) for c in list(str(i))]
            print i
            total += i
                

    print "total:\n", total

if __name__ == '__main__':
    start_time = time.time()
    main()
    print("--- %s seconds ---" % "%.2f" % (time.time() - start_time) )

    # 4.60seconds
